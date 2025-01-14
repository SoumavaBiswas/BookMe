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

    @model_validator(mode="before")
    def assign_book_id(cls, values):
        if not values.get('book_id'):
            values['book_id'] = str(uuid.uuid4())
        return values

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
    genre: Optional[str] = "Unknown"
    author: str = "Unknown"
    publisher: Optional[str] = "Unknown"
    price: int 

    @field_validator('price')
    def price_validator(cls, value):
        if value < 0:
            return ValueError("Price should be positive.")
        return value


    
