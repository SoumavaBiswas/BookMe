from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
import uuid


class Book(BaseModel):
    book_id: Optional[str] = None
    title: str
    genre: Optional[str] = "Unknown"
    author: str = "Unknown"
    isbn: str
    publisher: Optional[str] = "Unknown"
    price: int 

    class Config:
        arbitrary_types_allowed = True

    @field_validator('isbn')
    def isbn_validator(cls, value):
        if len(value.split("-")) < 4:
            return ValueError("Please provide correct ISBN.")
        return value

    @field_validator('price')
    def price_validator(cls, value):
        if value < 0:
            return ValueError("Price should be positive.")
        return value


class BookUpdateModel(BaseModel):
    genre: Optional[str] = None
    author: str = None
    publisher: Optional[str] = None
    price: int = 0

    @field_validator('price')
    def price_validator(cls, value):
        if value < 0:
            return ValueError("Price should be positive.")
        return value


    
