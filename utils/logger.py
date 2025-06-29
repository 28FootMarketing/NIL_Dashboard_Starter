# utils/logger.py
import datetime
import os

LOG_FILE = "/mnt/data/admin_change_log.txt"

def log_change(message: str, actor: str = "System"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {actor}: {message}\n"
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def get_log_history(limit=50):
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    return lines[-limit:]
