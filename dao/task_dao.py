from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class TaskDAO:
    @staticmethod
    def add_task(title, description, status="pending", deadline=None):
        data = {
            "title": title,
            "description": description,
            "status": status,
            "deadline": deadline,
            "created_at": datetime.now().isoformat()
        }
        supabase.table("tasks").insert(data).execute()

    @staticmethod
    def edit_task(task_id, **kwargs):
        kwargs['updated_at'] = datetime.now().isoformat()
        supabase.table("tasks").update(kwargs).eq("task_id", task_id).execute()

    @staticmethod
    def delete_task(task_id):
        supabase.table("tasks").delete().eq("task_id", task_id).execute()

    @staticmethod
    def get_task(task_id):
        return supabase.table("tasks").select("*").eq("task_id", task_id).execute().data

    @staticmethod
    def list_tasks(filter_by=None, value=None):
        query = supabase.table("tasks").select("*")
        if filter_by and value:
            query = query.eq(filter_by, value)
        result=query.execute()
        return result.data
