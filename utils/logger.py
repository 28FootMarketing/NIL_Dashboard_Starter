# utils/logger.py

from datetime import datetime

CHANGELOG_PATH = "changelog.txt"

def log_change(description: str, actor: str = "System"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ({actor}) {description}\n"
    with open(CHANGELOG_PATH, "a") as file:
        file.write(log_entry)
