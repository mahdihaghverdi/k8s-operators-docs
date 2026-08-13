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


def clone_operator(operator) -> str:
    """Cline the operator and return the path to its repo"""
    target = REPOS / operator["name"]

    if target.exists():
        shutil.rmtree(target)

    r = subprocess.run(
        [
            "git",
            "clone",
            f"https://github.com/mahdihaghverdi/{operator['name']}.git",
            str(target)
        ],
        check=True,
        capture_output=True,
    )
    print(r)

    return target


def main():
    operators = load_operators()

    REPOS.mkdir(exist_ok=True)

    for operator in operators:
        repo = clone_operator(operator)

    print(os.listdir(REPOS))


if __name__ == "__main__":
    main()