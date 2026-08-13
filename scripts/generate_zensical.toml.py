import logging
from pathlib import Path

logger = logging.getLogger("generator")

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
REPOS = ROOT / ".repos"

logger.error(REPOS)
logger.error(DOCS)
logger.error(REPOS)

print(REPOS)
print(DOCS)
print(REPOS)

