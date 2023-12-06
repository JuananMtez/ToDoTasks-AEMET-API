from sqlalchemy import Column, Integer, String
from app.config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    tasks = relationship("Task", cascade="save-update, delete")
