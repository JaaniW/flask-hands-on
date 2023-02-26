import datetime
from dataclasses import dataclass

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import Session
from sqlmodel import Session
from flask_sqlalchemy import SQLAlchemy


from application.database.db import Base, get_db

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
    def get_user_serialize(email):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(**data):
        db_obj = User(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

class Post(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    post = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)
    is_pinned = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True) 

    

    