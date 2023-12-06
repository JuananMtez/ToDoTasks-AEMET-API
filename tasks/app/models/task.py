from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Boolean
from app.config.database import Base
from sqlalchemy.orm import relationship

import enum


class PriorityEnum(enum.Enum):
    low = 0
    medium = 1
    high = 2


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    finalization_date = Column(DateTime, nullable=False)
    priority = Column('priority', Enum(PriorityEnum))
    is_finished = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    checklists = relationship("Checklist",  cascade="save-update, delete")
