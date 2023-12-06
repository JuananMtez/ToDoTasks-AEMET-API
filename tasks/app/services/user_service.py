from app.repositories.user_crud import UserCrud
from app.exceptions.user_exception import UserNotFound, UsernameAlreadyAssigned
from app.models.user import User


class UserService:
    def __init__(self, db):
        self.user_crud = UserCrud(db)

    def create_user(self, userPost):

        if self.user_crud.find_by_username(userPost.username) is not None:
            raise UsernameAlreadyAssigned

        user_db = User(username=userPost.username,
                       password=userPost.password,
                       tasks=[])

        return self.user_crud.save(user_db)

    def modify_username(self, user_id, usernameModify):

        user = self.user_crud.find_by_id(user_id)

        if user is None:
            raise UserNotFound

        if self.user_crud.find_by_username(usernameModify.username) is not None:
            raise UsernameAlreadyAssigned

        user.username = usernameModify.username

        return self.user_crud.save(user)

    def modify_password(self, user_id, passwordModify):
        user = self.user_crud.find_by_id(user_id)
        if user is None:
            raise UserNotFound

        user.password = passwordModify.password
        return self.user_crud.save(user)

    def delete_user(self, user_id):
        user = self.user_crud.find_by_id(user_id)
        if user is None:
            raise UserNotFound
        self.user_crud.delete(user)



    def find_all_user(self):
        return self.user_crud.find_all_users()

    def find_user(self, id_user):
        user = self.user_crud.find_by_id(id_user)

        if user is None:
            raise UserNotFound
        return user
