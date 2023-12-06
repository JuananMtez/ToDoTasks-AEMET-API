from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.config.database import Base

class Checklist(Base):
    __tablename__ = "checklist"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    action = Column(String, index=True, nullable=False)
    is_finished = Column(Boolean, nullable=False)
    task_id = Column(Integer, ForeignKey("task.id"))
