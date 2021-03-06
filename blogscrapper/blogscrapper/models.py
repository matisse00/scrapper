from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_scrapydb_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class ScrapyDB(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "app_post"

    id = Column(Integer, primary_key=True)
    text = Column('text', String)
    author = Column('author', String)
