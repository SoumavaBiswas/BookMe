from fastapi import APIRouter, HTTPException, status
from typing import List
from Models.Books import Book, BookUpdateModel


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
def get_books() -> List[Book]:
    res = []
    for book in books:
        book_obj = Book(**book)
        res.append(book_obj)
    return res


@AdminBookTransactionRouter.get('/books/{book_id}', response_model=Book)
def get_book(book_id: str) -> List[Book]:
    for book in books:
        if book["book_id"] == book_id:
            return Book(**book)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID: {book_id} not found.")


@AdminBookTransactionRouter.post('/books/', status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return {"message": f"New Book added with book id: {new_book['book_id']}"}

@AdminBookTransactionRouter.patch('/books/{book_id}', response_model=Book)
def update_book(book_id: str, book: BookUpdateModel):
    new_book = book.model_dump()
    for curr_book in books:
        if curr_book["book_id"] == book_id:
            curr_book["price"] = new_book["price"]
            curr_book["author"] = new_book["author"]
            curr_book["publisher"] = new_book["publisher"]
            return curr_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID: {book_id} not found.")


@AdminBookTransactionRouter.delete('/books/{book_id}')
def delete_book(book_id: str):
    for curr_book in books:
        if curr_book["book_id"] == book_id:
           books.remove(curr_book)
           return {"message": f"Successfully deleted book with {book_id}"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID: {book_id} not found.")
