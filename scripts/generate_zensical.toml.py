import logging
from pathlib import Path

logger = logging.getLogger("generator")

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
REPOS = ROOT / ".repos"

logger.info(REPOS)
logger.info(DOCS)
logger.info(REPOS)

