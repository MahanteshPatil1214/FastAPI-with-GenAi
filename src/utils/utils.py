import json
from pathlib import Path

# Assumes products.json is located in src/data/products.json
# If your products.json is in the project root, change to: Path(__file__).resolve().parent.parent.parent / "products.json"
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "products.json"

def getAllProducts():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)