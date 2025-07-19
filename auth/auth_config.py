from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
# /auth/auth_config.py

# Comment out or remove this import if Supabase is not used
# from supabase import create_client

supabase = None  # Placeholder
