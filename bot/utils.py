import logging
import json
import time
from filelock import FileLock
from pathlib import Path

logger = logging.getLogger(__name__)

# locks for safe file access
BASE_DIR = Path(__file__).resolve().parent.parent
HISTORY_LOCK = FileLock(str(BASE_DIR / "chat_history.json") + ".lock")

def safe_load_json(file_path, max_attempts=5):
    """Tries to safely load a JSON file, even if other processes are writing to it."""
    if not file_path.exists():
        return {}

    for attempt in range(max_attempts):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return {int(k) if k.isdigit() else k: v for k, v in data.items()}
                return data
        except (json.JSONDecodeError, OSError, BlockingIOError, PermissionError) as e:
            if attempt < max_attempts - 1:
                logger.warning(f"File {file_path.name} busy or error (Attempt {attempt+1}/{max_attempts}): {e}")
                time.sleep(0.05)
            else:
                logger.error(f"Critical: Could not load {file_path.name} after {max_attempts} attempts.")
        
        except Exception as e:
            logger.error(f"Unexpected error while loading {file_path.name}: {e}")
            break    
    return {}