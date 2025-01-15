from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import uuid

Base = declarative_base()

class BookDB(Base):
    __tablename__ = "books"
    book_id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    title= Column(String)
    genre= Column(String, default="Unknown")
    author= Column(String, default="Unknown")
    isbn= Column(String, unique=True)
    publisher= Column(String, default="Unknown")
    price= Column(Integer)