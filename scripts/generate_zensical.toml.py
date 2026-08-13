import logging
import os
from pathlib import Path

logger = logging.getLogger("generator")

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
REPOS = ROOT / ".repos"

for thing in (ROOT, DOCS, REPOS):
    print(os.listdir(thing))
