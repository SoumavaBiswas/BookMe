from sqlalchemy.orm import Session
from models.Book_db import BookDB
from models.Books import Book, BookUpdateModel
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import IntegrityError
import psycopg2

def add_book(book: Book, db: Session):
    book_obj = book.model_dump()
    db_book = BookDB(**book_obj)
    try:
        db.add(db_book)
        db.commit()
        return {"message": f"Book added with book id: {db_book.book_id}"}
    except IntegrityError as e:
        db.rollback()
        if isinstance(e.orig, psycopg2.errors.UniqueViolation):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"ISBN: {book.isbn} already exists.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="An Intefgrity error occured.")

def get_books(db: Session):
    return db.query(BookDB).all()

def get_book(book_id: str, db: Session):
    book_from_db = db.query(BookDB).filter(BookDB.book_id==book_id).first()
    if not book_from_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID: {book_id} not found.")
    return book_from_db

def update_book(book_id: str, book: BookUpdateModel, db: Session):
    db_book = get_book(book_id, db)
    db_book.author = book.author or db_book.author
    db_book.genre = book.genre or db_book.genre
    db_book.publisher = book.publisher or db_book.publisher
    db_book.price = book.price or db_book.price
    db.commit()
    return db_book

def delete_book(book_id: str, db: Session):
    books = get_books(db)
    for curr_book in books:
        if curr_book.book_id == book_id:
           db.delete(curr_book)
           db.commit()
           return {"message": f"Successfully deleted book with {book_id}"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID: {book_id} not found.")
