from db.base import engine
from models.Book_db import Base

Base.metadata.create_all(engine)