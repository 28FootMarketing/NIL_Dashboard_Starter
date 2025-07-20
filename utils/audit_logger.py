import json
import os
from datetime import datetime

LOG_FILE = "./logs/audit_log.json"

def log_event(event_type, user_email, message):
    log_entry = {
        "event_type": event_type,
        "user": user_email,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }

    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                json.dump([log_entry], f, indent=4)
        else:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
            logs.append(log_entry)
            with open(LOG_FILE, "w") as f:
                json.dump(logs, f, indent=4)
    except Exception as e:
        print(f"[Audit Log Error] {e}")
