import json
from pathlib import Path

class DataHandler:

    def __init__(self, filepath: str):
        self.file = Path(filepath)

    def read(self):
        if not self.file.exists():
            return []
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def write(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)