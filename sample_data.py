from pathlib import Path
import datasets as hfds


output_dir = Path("examples/source_documents")
output_dir.mkdir(parents=True, exist_ok=True)

ds = hfds.load_dataset("HuggingFaceFW/fineweb-2", name="deu_Latn", split="train", data_files="data/deu_Latn/train/000_00000.parquet")
# ds = ds.select(range(20))

selected_examples = [
    5,
    6,
    7,
    12,
    15
]
ds = ds.select(selected_examples)

for idx, example in enumerate(ds):
    with open(output_dir / f"fw2_deu_Latn_{idx}.txt", "w") as f:
        f.write(example['text'])


ds = hfds.load_dataset("HuggingFaceFW/fineweb-edu", split="train", data_files="sample/10BT/000_00000.parquet")
# ds = ds.select(range(20))

selected_examples = [
    0,
    2,
    3,
    4,
    5
]
ds = ds.select(selected_examples)

for idx, example in enumerate(ds):
    with open(output_dir / f"fw_eng_Latn_{idx}.txt", "w") as f:
        f.write(example['text'])


# ds = hfds.load_dataset("HuggingFaceFW/finepdfs", name="deu_Latn", split="train", data_files="data/deu_Latn/train/000_00000.parquet")
# ds = ds.select(range(20))

# for idx, example in enumerate(ds):
#     with open(output_dir / f"fpdfs_deu_Latn_{idx}.txt", "w") as f:
#         f.write(example['text'])


# ds = hfds.load_dataset("HuggingFaceFW/finepdfs", name="eng_Latn", split="train", data_files="data/eng_Latn/train/000_00000.parquet")
# ds = ds.select(range(20))

# for idx, example in enumerate(ds):
#     with open(output_dir / f"fpdfs_eng_Latn_{idx}.txt", "w") as f:
#         f.write(example['text'])




