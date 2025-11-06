"""
Collect generated synthetic data into two review-facing markdown documents (EN and DE).

The script:
- Reads prompt explanations from README (English "Output data" and German details block)
- Recursively scans examples/synthetic_data for generated .md files
- Splits documents by language (based on filename containing _eng_ vs _deu_)
- Organizes outputs per document: explanations first, then each source doc with all synthesized variants
- Writes two consolidated markdown files suitable for non-technical review

Usage:
  python collect_for_review.py \
    --data-dir examples/synthetic_data \
    --readme README.md \
    --out-dir examples/review
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


PROMPT_ORDER = [
    "summary",
    "qa",
    "edu_material",
    "exams",
    "active_reading",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect generated outputs into review-facing overview documents.")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("examples/synthetic_data"),
        help="Root directory containing generated prompt outputs.",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path("README.md"),
        help="Path to README containing prompt explanations.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("examples/review"),
        help="Directory to write consolidated markdown documents.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_english_explanations(readme_text: str) -> Dict[str, str]:
    # Extract section between '## Output data' and the next '## ' or details block
    start_marker = "## Output data"
    end_markers = ["\n## ", "<details>"]
    start = readme_text.find(start_marker)
    if start == -1:
        return {}
    tail = readme_text[start:]
    # find earliest end marker occurrence after the start
    ends = [i for i in (tail.find(m) for m in end_markers) if i != -1 and i > 0]
    if ends:
        end = min(ends)
        chunk = tail[:end]
    else:
        chunk = tail
    return _extract_prompt_sections(chunk)


def extract_german_explanations(readme_text: str) -> Dict[str, str]:
    # Extract content inside the German details block
    details_start = "<summary>Deutsch: Ausgabedaten</summary>"
    details_end = "</details>"
    sidx = readme_text.find(details_start)
    eidx = readme_text.find(details_end, sidx + 1) if sidx != -1 else -1
    if sidx == -1 or eidx == -1:
        return {}
    chunk = readme_text[sidx:eidx]
    return _extract_prompt_sections(chunk)


def _extract_prompt_sections(chunk: str) -> Dict[str, str]:
    # Parse '### <prompt>' headings and capture following paragraph(s) until next '### '
    lines = chunk.splitlines()
    result: Dict[str, str] = {}
    current_key: str | None = None
    buffer: List[str] = []
    for line in lines:
        if line.startswith("### "):
            # flush previous
            if current_key is not None:
                result[current_key] = _clean_text("\n".join(buffer))
                buffer = []
            heading = line[len("### "):].strip()
            key = heading.strip().lower()
            current_key = key
        else:
            if current_key is not None:
                buffer.append(line)
    if current_key is not None:
        result[current_key] = _clean_text("\n".join(buffer))
    return result


def _clean_text(text: str) -> str:
    # Trim leading/trailing whitespace and collapse leading blank line
    cleaned = text.strip()
    return cleaned


def iter_generated_markdowns(root: Path) -> Iterable[Path]:
    # Support both patterns:
    # - examples/synthetic_data/<prompt>/<file>.md
    # - examples/synthetic_data/<prompt>/<prompt>/<file>.md
    if not root.exists():
        return []
    return root.rglob("*.md")


def get_prompt_key(md_path: Path) -> str:
    parent = md_path.parent.name
    gp = md_path.parent.parent.name if md_path.parent.parent != md_path.parent else ""
    if parent == gp and parent:
        return parent
    return parent


def get_language_from_filename(md_path: Path) -> str | None:
    name = md_path.name
    if "_eng_" in name:
        return "en"
    if "_deu_" in name:
        return "de"
    return None


def group_by_prompt_and_language(paths: Iterable[Path]) -> Tuple[Dict[str, Dict[str, List[Path]]], Dict[str, Dict[str, List[Path]]]]:
    # Returns (by_lang["en"][prompt] -> [paths], by_lang["de"][prompt] -> [paths])
    by_lang: Dict[str, Dict[str, List[Path]]] = {"en": {}, "de": {}}
    for p in paths:
        lang = get_language_from_filename(p)
        if lang not in ("en", "de"):
            continue
        prompt = get_prompt_key(p)
        by_lang.setdefault(lang, {}).setdefault(prompt, []).append(p)
    # sort each file list by name for stable output
    for lang in ("en", "de"):
        for prompt in list(by_lang[lang].keys()):
            by_lang[lang][prompt] = sorted(by_lang[lang][prompt], key=lambda q: q.name)
    return by_lang, by_lang


def build_intro(language: str) -> str:
    if language == "en":
        return (
            "# Synthetic Data for Review\n\n"
            "This document consolidates synthetic materials created from publicly available source texts. "
            "It is intended to help reviewers quickly understand what was generated, in which formats, and how each output is meant to be used.\n\n"
            "Contents (at a glance):\n\n"
            "- Prompt explanations: Brief description, purpose, and format of outputs.\n"
            "- Per document: Source file, then all generated variants in a fixed order:\n"
            "  Summary, Q&A, Educational Material, Exams, Active Reading.\n\n"
            "The content is presented in the original language of the source document.\n\n"
        )
    else:
        return (
            "# Synthetische Daten zur Durchsicht\n\n"
            "Dieses Dokument bündelt synthetisch erzeugte Materialien basierend auf öffentlich verfügbaren Ausgangstexten. "
            "Es dient dazu, schnell zu verstehen, was erzeugt wurde, in welchen Formaten, und wofür die Inhalte gedacht sind.\n\n"
            "Inhalt (kurze Orientierung):\n\n"
            "- Erläuterungen zu den Prompt-Typen: Kurzbeschreibung, Zweck und Format der Ausgaben.\n"
            "- Pro Dokument: Quelldatei, danach alle erzeugten Varianten in fester Reihenfolge: \n"
            "  Zusammenfassung, Fragen & Antworten, Lernmaterial, Prüfungen, Aktives Lesen.\n\n"
            "Die Inhalte sind in der Originalsprache des jeweiligen Quelldokuments dargestellt.\n\n"
        )


def titlecase_prompt(key: str) -> str:
    mapping = {
        "summary": "Summary",
        "qa": "Q&A",
        "edu_material": "Educational Material",
        "exams": "Exams",
        "active_reading": "Active Reading",
    }
    return mapping.get(key, key.title())


def titlecase_prompt_de(key: str) -> str:
    mapping = {
        "summary": "Zusammenfassung",
        "qa": "Fragen & Antworten",
        "edu_material": "Lernmaterial",
        "exams": "Prüfungen",
        "active_reading": "Aktives Lesen",
    }
    return mapping.get(key, key.title())


def add_prompt_explanations_section(language: str, explanations: Dict[str, str]) -> List[str]:
    content: List[str] = []
    section_title = "## Prompt explanations" if language == "en" else "## Erläuterungen zu den Prompt-Typen"
    content.append(section_title)
    for key in PROMPT_ORDER:
        heading = titlecase_prompt(key) if language == "en" else titlecase_prompt_de(key)
        expl = explanations.get(key, "").strip()
        if not expl:
            continue
        content.append(f"### {heading}")
        content.append(expl)
        content.append("")
    return content


def stem_from_filename(p: Path) -> str:
    return p.stem


def group_by_language_then_stem(paths: Iterable[Path]) -> Dict[str, Dict[str, Dict[str, Path]]]:
    by_lang: Dict[str, Dict[str, Dict[str, Path]]] = {"en": {}, "de": {}}
    for p in paths:
        lang = get_language_from_filename(p)
        if lang not in ("en", "de"):
            continue
        stem = stem_from_filename(p)
        prompt = get_prompt_key(p)
        by_lang.setdefault(lang, {}).setdefault(stem, {})[prompt] = p
    return by_lang


def assemble_document(language: str, by_stem: Dict[str, Dict[str, Path]], explanations: Dict[str, str]) -> str:
    parts: List[str] = [build_intro(language)]
    parts.extend(add_prompt_explanations_section(language, explanations))
    if parts and not parts[-1].endswith("\n\n"):
        parts.append("")
    stems = sorted(by_stem.keys())
    for idx, stem in enumerate(stems):
        parts.append("---")
        doc_title = (
            f"#### Document {idx}: {stem}" if language == "en" else f"#### Dokument {idx}: {stem}"
        )
        parts.append(doc_title)
        # Include source document verbatim
        src_heading = "### Source document" if language == "en" else "### Quelldokument"
        parts.append(src_heading)
        src_path = Path("examples/source_documents") / f"{stem}.txt"
        if src_path.exists():
            parts.append(read_text(src_path))
        else:
            missing = (
                f"[Source file not found: {src_path}]" if language == "en" else f"[Quelldatei nicht gefunden: {src_path}]"
            )
            parts.append(missing)
        parts.append("")
        prompt_to_path = by_stem[stem]
        for key in PROMPT_ORDER:
            path = prompt_to_path.get(key)
            if not path:
                continue
            heading = titlecase_prompt(key) if language == "en" else titlecase_prompt_de(key)
            parts.append(f"### {heading}")
            parts.append(read_text(path))
            parts.append("")
    return "\n".join(parts).strip() + "\n"


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    readme_text = read_text(args.readme)
    en_expl = extract_english_explanations(readme_text)
    de_expl = extract_german_explanations(readme_text)

    all_md = list(iter_generated_markdowns(args.data_dir))
    by_lang_and_stem = group_by_language_then_stem(all_md)
    en_grouped = by_lang_and_stem.get("en", {})
    de_grouped = by_lang_and_stem.get("de", {})

    en_doc = assemble_document("en", en_grouped, en_expl)
    de_doc = assemble_document("de", de_grouped, de_expl)

    en_path = args.out_dir / "review_en.md"
    de_path = args.out_dir / "review_de.md"
    en_path.write_text(en_doc, encoding="utf-8")
    de_path.write_text(de_doc, encoding="utf-8")
    print(f"Wrote: {en_path}")
    print(f"Wrote: {de_path}")


if __name__ == "__main__":
    main()


