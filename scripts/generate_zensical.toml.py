import logging
import os
import shutil
import subprocess
import tomllib
from pathlib import Path

logger = logging.getLogger("generator")

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
REPOS = ROOT / ".repos"

def load_operators():
    with open(ROOT / "operators.config.toml", "rb") as f:
        return tomllib.load(f)["operators"]


def main():
    operators = load_operators()
    REPOS.mkdir(exist_ok=True)
    print(os.listdir(ROOT))


if __name__ == "__main__":
    main()