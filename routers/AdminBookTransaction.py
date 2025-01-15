from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from models.Books import Book, BookUpdateModel
from sqlalchemy.orm import Session
from db.base import get_db
from dao import book_dao



AdminBookTransactionRouter = APIRouter()
books = [
    {
        "book_id": "1",
        "title": "The Catcher in the Rye",
        "genre": "Fiction",
        "author": "J.D. Salinger",
        "isbn": "978-0-316-76948-0",
        "publisher": "Little, Brown and Company",
        "price": 499
    },
    {
        "book_id": "2",
        "title": "1984",
        "genre": "Dystopian",
        "author": "George Orwell",
        "isbn": "978-0-452-28423-4",
        "publisher": "Plume",
        "price": 399
    },
    {
        "book_id": "3",
        "title": "To Kill a Mockingbird",
        "genre": "Classic",
        "author": "Harper Lee",
        "isbn": "978-0-06-112008-4",
        "publisher": "J.B. Lippincott & Co.",
        "price": 599
    },
    {
        "book_id": "4",
        "title": "The Great Gatsby",
        "genre": "Classic",
        "author": "F. Scott Fitzgerald",
        "isbn": "978-0-7432-7356-5",
        "publisher": "Scribner",
        "price": 349
    },
    {
        "book_id": "5",
        "title": "Moby-Dick",
        "genre": "Adventure",
        "author": "Herman Melville",
        "isbn": "978-0-14-243724-7",
        "publisher": "Penguin Classics",
        "price": 450
    },
    {
        "book_id": "6",
        "title": "Pride and Prejudice",
        "genre": "Romance",
        "author": "Jane Austen",
        "isbn": "978-0-19-953556-9",
        "publisher": "Oxford University Press",
        "price": 299
    },
    {
        "book_id": "7",
        "title": "The Hobbit",
        "genre": "Fantasy",
        "author": "J.R.R. Tolkien",
        "isbn": "978-0-618-00221-3",
        "publisher": "Houghton Mifflin Harcourt",
        "price": 799
    },
    {
        "book_id": "8",
        "title": "War and Peace",
        "genre": "Historical Fiction",
        "author": "Leo Tolstoy",
        "isbn": "978-0-14-044793-4",
        "publisher": "Penguin Classics",
        "price": 1299
    },
    {
        "book_id": "9",
        "title": "The Alchemist",
        "genre": "Philosophical",
        "author": "Paulo Coelho",
        "isbn": "978-0-06-112241-5",
        "publisher": "HarperOne",
        "price": 499
    },
    {
        "book_id": "10",
        "title": "The Road",
        "genre": "Post-apocalyptic",
        "author": "Cormac McCarthy",
        "isbn": "978-0-307-38789-9",
        "publisher": "Vintage International",
        "price": 599
    }
]


@AdminBookTransactionRouter.get('/books')
def get_books(db: Session = Depends(get_db)) -> List[Book]:
    return book_dao.get_books(db=db)

@AdminBookTransactionRouter.get('/books/{book_id}', response_model=Book)
def get_book(book_id: str, db: Session = Depends(get_db)) -> List[Book]:
   return book_dao.get_book(book_id=book_id, db=db)

@AdminBookTransactionRouter.post('/books/', status_code=status.HTTP_201_CREATED)
def add_book(book: Book, db: Session = Depends(get_db)):
    print(book)
    return book_dao.add_book(book=book, db=db)

@AdminBookTransactionRouter.patch('/books/{book_id}', response_model=Book)
def update_book(book_id: str, book: BookUpdateModel, db: Session = Depends(get_db)):
    return book_dao.update_book(book_id=book_id, book=book, db=db)


@AdminBookTransactionRouter.delete('/books/{book_id}')
def delete_book(book_id: str, db: Session = Depends(get_db)):
    return book_dao.delete_book(book_id=book_id, db=db)