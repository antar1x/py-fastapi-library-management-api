from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from db import models
from db.models import Author


def get_all_authors(db: Session, author_id: int) -> Author:
    return db.scalar(select(models.Author).where(Author.id == author_id))