from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_to_supabase(user_email, query, response, metadata={}):
    data = {
        "email": user_email,
        "query": query,
        "response": response,
        "metadata": metadata
    }
    try:
        result = supabase.table("nil_logs").insert(data).execute()
        return result
    except Exception as e:
        return {"error": str(e)}

