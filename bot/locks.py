# locks.py
from filelock import FileLock
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
HISTORY_LOCK = FileLock(str(BASE_DIR / "chat_history.json") + ".lock")