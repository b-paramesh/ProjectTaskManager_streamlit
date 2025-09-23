from dao.user_dao import UserDAO

class UserService:
    @staticmethod
    def create_user(username, email, password_hash):
        UserDAO.add_user(username, email, password_hash)

    @staticmethod
    def update_user(user_id, **kwargs):
        UserDAO.edit_user(user_id, **kwargs)

    @staticmethod
    def remove_user(user_id):
        UserDAO.delete_user(user_id)

    @staticmethod
    def get_user_info(user_id):
        return UserDAO.get_user(user_id)

    @staticmethod
    def list_all_users():
        return UserDAO.list_users()
