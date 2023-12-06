from app.models.user import User


class UserCrud:
    def __init__(self, db):
        self.db = db

    def find_by_id(self, id):
        return self.db.query(User).filter(User.id == id).first()

    def find_all_users(self):
        return self.db.query(User).all()

    def find_by_username(self, username):
        return self.db.query(User).filter(User.username == username).first()

    def exists_by_id(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first() is not None

    def delete(self, user):
        self.db.delete(user)
        self.db.commit()

    def save(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user