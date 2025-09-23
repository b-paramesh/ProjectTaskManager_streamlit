from dao.task_dao import TaskDAO
from dao.status_history_dao import TaskStatusHistoryDAO

class TaskService:
    @staticmethod
    def create_task(title, description, status="pending", deadline=None):
        TaskDAO.add_task(title, description, status, deadline)

    @staticmethod
    def update_task(task_id, **kwargs):
        TaskDAO.edit_task(task_id, **kwargs)

    @staticmethod
    def delete_task(task_id):
        TaskDAO.delete_task(task_id)

    @staticmethod
    def change_status(task_id, status):
        TaskDAO.edit_task(task_id, status=status)
        TaskStatusHistoryDAO.add_status_history(task_id, status)

    @staticmethod
    def list_tasks(filter_by=None, value=None):
        return TaskDAO.list_tasks(filter_by, value)
