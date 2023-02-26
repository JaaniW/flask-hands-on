from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from config import Config

config = Config()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        return db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
