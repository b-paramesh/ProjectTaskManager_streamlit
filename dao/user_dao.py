import os
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class UserDAO:
    @staticmethod
    def add_user(username, email, password_hash):
        data = {
            "username": username,
            "email": email,
            "password_hash": password_hash,
             "created_at": datetime.now().isoformat()
        }
        supabase.table("users").insert(data).execute()

    @staticmethod
    def edit_user(user_id, **kwargs):
        kwargs['updated_at'] = datetime.now().isoformat()
        supabase.table("users").update(kwargs).eq("user_id", user_id).execute()

    @staticmethod
    def delete_user(user_id):
        supabase.table("users").delete().eq("user_id", user_id).execute()

    @staticmethod
    def get_user(user_id):
        return supabase.table("users").select("*").eq("user_id", user_id).execute().data

    @staticmethod
    def list_users():
        return supabase.table("users").select("*").execute().data
