import os

ENTRY_PATH = "/output/entry.txt"

os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
with open(ENTRY_PATH, "w", encoding="utf-8") as f:
    f.write("B")
