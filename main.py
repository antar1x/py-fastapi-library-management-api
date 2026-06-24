from fastapi import FastAPI, HTTPException

from db.engine import Base, engine, CurrentSession
from schemas import AuthorCreate, Author, BookRead, BookCreate
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/authors/", response_model=Author)
def create_author(author: AuthorCreate, db: CurrentSession):
    return crud.create_author(author=author, db=db)


@app.get("/authors/", response_model=list[Author])  # ← list
def get_authors(db: CurrentSession, skip: int = 0, limit: int = 10):
    return crud.get_all_authors(db=db, skip=skip, limit=limit)


@app.get("/authors/{author_id}", response_model=Author)
def get_author(author_id: int, db: CurrentSession):
    author = crud.get_author(author_id=author_id, db=db)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.post("/authors/{author_id}/books/", response_model=BookRead)
def create_book(author_id: int, book: BookCreate, db: CurrentSession):
    author = crud.get_author(author_id=author_id, db=db)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return crud.create_book(book=book, db=db)


@app.get("/books/", response_model=list[BookRead])  # ← list
def get_books(
    db: CurrentSession,
    skip: int = 0,
    limit: int = 10,
    author_id: int | None = None
):
    return crud.get_books(db=db, skip=skip, limit=limit, author_id=author_id)
