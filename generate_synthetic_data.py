"""
Script to generate synthetic data from source documents using OpenRouter models.

Features:
- Loads all documents from an input directory (default: examples/source_documents)
- Formats a prompt from prompts.py using a selected key (default: summary)
- Uses the OpenRouter (OpenAI-compatible) SDK to generate responses
- Saves results to an output directory (default: examples/synthetic_data)

Environment:
- Requires OPENROUTER_API_KEY to be set in your environment

Usage examples:
  python generate_synthetic_data.py \
    --prompt-key summary \
    --model gpt-5-mini \
    --input-dir examples/source_documents \
    --output-dir examples/synthetic_data/summary
"""

import argparse
import asyncio
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple

from openai import AsyncOpenAI

import prompts as prompt_module

try:
    from tqdm import tqdm  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    tqdm = None  # type: ignore


@dataclass
class GenerationConfig:
    model_name: str
    prompt_key: str
    input_dir: Path
    output_dir: Path
    max_concurrency: int


def parse_args() -> GenerationConfig:
    prompt_keys = sorted(list(prompt_module.PROMPTS.keys()))

    parser = argparse.ArgumentParser(description="Generate synthetic data from source documents using OpenRouter models.")
    parser.add_argument(
        "--model",
        dest="model_name",
        default="gpt-5-mini",
        help="OpenRouter model to use (default: gpt-5-mini)",
    )
    parser.add_argument(
        "--prompt-key",
        dest="prompt_key",
        choices=prompt_keys,
        default="summary",
        help=f"Prompt key to use from prompts.py (choices: {', '.join(prompt_keys)})",
    )
    parser.add_argument(
        "--input-dir",
        dest="input_dir",
        type=Path,
        default=Path("examples/source_documents"),
        help="Directory containing input documents (default: examples/source_documents)",
    )
    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        type=Path,
        default=Path("examples/synthetic_data"),
        help="Directory to write generated outputs (default: examples/synthetic_data)",
    )
    parser.add_argument(
        "--max-concurrency",
        dest="max_concurrency",
        type=int,
        default=10,
        help="Maximum number of concurrent API requests (default: 10)",
    )

    args = parser.parse_args()
    return GenerationConfig(
        model_name=args.model_name,
        prompt_key=args.prompt_key,
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        max_concurrency=args.max_concurrency,
    )


def validate_environment() -> None:
    if not os.environ.get("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY is not set in the environment.", file=sys.stderr)
        sys.exit(2)


def iter_text_files(input_dir: Path) -> Iterable[Path]:
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory does not exist or is not a directory: {input_dir}")
    for path in sorted(input_dir.iterdir()):
        if path.is_file() and path.suffix.lower() in {".txt", ".md"}:
            yield path


def read_document(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def format_prompt(prompt_key: str, document_text: str) -> str:
    try:
        template = prompt_module.PROMPTS[prompt_key]
    except KeyError as exc:
        raise KeyError(f"Unknown prompt key: {prompt_key}. Available: {sorted(prompt_module.PROMPTS.keys())}") from exc
    return template.format(document=document_text)


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


async def generate_response_async(client: AsyncOpenAI, model_name: str, prompt_text: str) -> str:
    # Using Chat Completions API for compatibility
    completion = await client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt_text},
        ],
    )
    message = completion.choices[0].message
    content = (message.content or "").strip()
    if not content:
        raise RuntimeError("Empty content returned by the model.")
    return content


def output_path_for(input_path: Path, base_output_dir: Path, prompt_key: str) -> Path:
    # Organize outputs by prompt key, keep same base filename, write as .md
    prompt_dir = base_output_dir / prompt_key
    ensure_directory(prompt_dir)
    return prompt_dir / (input_path.stem + ".md")


async def process_documents_async(cfg: GenerationConfig) -> List[Tuple[Path, Path]]:
    validate_environment()
    ensure_directory(cfg.output_dir)

    base_url = os.environ.get("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
    api_key = os.environ["OPENROUTER_API_KEY"]
    client = AsyncOpenAI(base_url=base_url, api_key=api_key)

    semaphore = asyncio.Semaphore(cfg.max_concurrency)
    processed: List[Tuple[Path, Path]] = []
    use_progress = tqdm is not None

    async def process_one(doc_path: Path) -> Tuple[Path, Path] | None:
        async with semaphore:
            try:
                document_text = read_document(doc_path)
                prompt_text = format_prompt(cfg.prompt_key, document_text)
                response_markdown = await generate_response_async(client, cfg.model_name, prompt_text)
                out_path = output_path_for(doc_path, cfg.output_dir, cfg.prompt_key)
                out_path.write_text(response_markdown, encoding="utf-8")
                if not use_progress:
                    print(f"Generated: {doc_path.name} -> {out_path}")
                return (doc_path, out_path)
            except Exception as exc:  # noqa: BLE001 - per-file processing
                print(f"Error processing {doc_path}: {exc}", file=sys.stderr)
                return None

    doc_paths = list(iter_text_files(cfg.input_dir))
    tasks = [asyncio.create_task(process_one(doc_path)) for doc_path in doc_paths]
    if use_progress:
        results: List[Tuple[Path, Path] | None] = []
        assert tqdm is not None
        with tqdm(total=len(tasks), desc="Generating", unit="file") as pbar:  # type: ignore
            for coro in asyncio.as_completed(tasks):
                res = await coro
                results.append(res)
                pbar.update(1)  # type: ignore
    else:
        results = await asyncio.gather(*tasks, return_exceptions=False)
    for result in results:
        if result is not None:
            processed.append(result)
    return processed


def main() -> None:
    cfg = parse_args()
    print(
        f"Running generation with model={cfg.model_name}, prompt_key={cfg.prompt_key}, "
        f"input_dir={cfg.input_dir}, output_dir={cfg.output_dir}"
    )
    processed = asyncio.run(process_documents_async(cfg))
    if not processed:
        print("No documents processed.", file=sys.stderr)
        sys.exit(1)
    print(f"Done. Wrote {len(processed)} files to {cfg.output_dir}")


if __name__ == "__main__":
    main()


