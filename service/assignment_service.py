from dao.assignment_dao import TaskAssignmentDAO

class AssignmentService:
    @staticmethod
    def assign_task(task_id, user_id):
        TaskAssignmentDAO.assign_task(task_id, user_id)

    @staticmethod
    def list_assignments():
        return TaskAssignmentDAO.list_assignments()
