from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class TaskStatusHistoryDAO:
    @staticmethod
    def add_status_history(task_id, status):
        data = {
            "task_id": task_id,
            "status": status,
            "changed_at": datetime.now().isoformat()
        }
        supabase.table("task_status_history").insert(data).execute()

    @staticmethod
    def list_history(task_id=None):
        query = supabase.table("task_status_history")
        if task_id:
            query = query.eq("task_id", task_id)
        return query.select("*").execute().data
