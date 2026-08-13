import logging
import os
import shutil
import tomllib
from pathlib import Path

logger = logging.getLogger("generator")

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"


def load_operators():
    with open(ROOT / "operators.config.toml", "rb") as f:
        return tomllib.load(f)["operators"]


def copy_docs(operator_name: str):
    source = ROOT / operator_name / "docs"
    target = DOCS / operator_name
    shutil.copytree(source, target)


def main():
    operators = load_operators()
    for operator in operators:
        copy_docs(operator)

    print(os.listdir(DOCS))

if __name__ == "__main__":
    main()