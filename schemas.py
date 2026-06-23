import datetime
from ast import List

from pydantic import BaseModel, ConfigDict


class BookType(BaseModel):
    title: str
    summary: str
    publication_date: datetime.date
    author_id: int

class BookCreate(BookType):
    pass

class Book(BookType):
    id: int

    model_config = ConfigDict(from_attributes=True)

class AuthorType(BaseModel):
    name: str
    bio: str

class AuthorCreate(AuthorType):
    pass

class Author(BaseModel):
    id: int
    books: List[Book] = []

    model_config = ConfigDict(from_attributes=True)

