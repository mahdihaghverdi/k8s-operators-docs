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

    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            f"https://github.com/mahdihaghverdi/{operator['name']}.git",
            str(target)
        ],
        check=True,
    )

    return target


def main():
    operators = load_operators()

    REPOS.mkdir(exist_ok=True)

    for operator in operators:
        repo = clone_operator(operator)

    print(os.listdir(REPOS))


if __name__ == "__main__":
    main()