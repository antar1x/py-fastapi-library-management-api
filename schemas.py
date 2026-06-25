import datetime
from pydantic import BaseModel, ConfigDict, Field


class BookType(BaseModel):
    title: str
    summary: str
    publication_date: datetime.date
    author_id: int


class BookCreate(BookType):
    pass


class BookRead(BookType):
    id: int
    model_config = ConfigDict(from_attributes=True)


class AuthorType(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorType):
    pass


class Author(AuthorType):
    id: int
    books: list[BookRead] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)
