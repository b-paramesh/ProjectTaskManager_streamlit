from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class TaskAssignmentDAO:
    @staticmethod
    def assign_task(task_id, user_id):
        data = {
            "task_id": task_id,
            "user_id": user_id,
            "assigned_at": datetime.now().isoformat()
        }
        supabase.table("task_assignments").insert(data).execute()

    @staticmethod
    def list_assignments():
        return supabase.table("task_assignments").select("*").execute().data
