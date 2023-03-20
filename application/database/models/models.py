import datetime
from dataclasses import dataclass

from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.orm import Session, relationship
from sqlmodel import Session
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


from application.database.db import Base, get_db

db = get_db()



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String(50), index=True, unique=True)
    email = Column(String(150), unique=True, index=True)
    password = Column(String(250))
    date_of_birth = Column(DateTime(), default=datetime.datetime.utcnow())
    is_admin = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=True)
    posts = relationship('Post', backref='user')

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

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post = Column(Text, nullable=False)
    image = Column(String(100))
    created_at = Column(DateTime(), default=datetime.datetime.utcnow())
    updated_at = Column(DateTime(), default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
    is_deleted = Column(Boolean, default=False)
    is_pinned = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True) 

    

    @staticmethod
    def create_post(data):
        db_obj = Post(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @staticmethod
    def update_post(post_id, data):
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return "No post available", 404
        
        post.post = data.get("post")
        post.image = data.get("image")
        db.commit()
        return {"post_id": post.id, "post_image": post.image, "post_text": post.text}, 202
    

    @staticmethod
    def delete_post(post_id):
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return "No post available", 404
        
        db.delete(post)
        return "", 204
    
    @staticmethod
    def get_post(post_id, data):
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return "Post not available", 404
        
        post.post = data.get("post")
        post.image = data.get("image")
        db.commit()
        return {"post_id": post.id, "post_image": post.image, "post_text": post.text}, 202
    