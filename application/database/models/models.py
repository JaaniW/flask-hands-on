import datetime
from application.database.db import Base
from sqlmodel import Session
from sqlalchemy.orm import Session
from application.database.db import get_db

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)

from dataclasses import dataclass

db = get_db()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String(50), index=True, unique=True)
    email = Column(String(150), unique=True, index=True)
    password = Column(String(250))
    date_of_birth = Column(DateTime(), default=datetime.datetime.utcnow(), index=True)
    is_admin = Column(Boolean, default=True) 
    is_staff = Column(Boolean, default=True) 
    is_superuser = Column(Boolean, default=True)

    @staticmethod
    def get_user_serialize(id):
        return db.query(User).filter(User.id==id).first().__dict__
    
    @staticmethod
    def create_user(**data):
        db_obj = User(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
