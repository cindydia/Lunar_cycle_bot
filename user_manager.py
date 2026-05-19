import json
from datetime import datetime


class UserManager:
    FILE_NAME = "users.json"

    @staticmethod
    def load_users():

        try:
            with open(UserManager.FILE_NAME, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_user(user_id, username):

        try:
            users = UserManager.load_users()

            users[str(user_id)] = {
                "username": username,
                "joined": str(datetime.utcnow())
            }

            with open(UserManager.FILE_NAME, "w") as file:
                json.dump(users, file, indent=4)

        except Exception:
            pass

    @staticmethod
    def get_user_count():

        try:
            return len(UserManager.load_users())
        except Exception:
            return 0