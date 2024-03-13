from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid

from routes.users import user

app = FastAPI()

books = []


class Book(BaseModel):
    id: Optional[str]
    title: str
    description: Text
    author: str
    pages: int
    editorial: Optional[str]
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


app.include_router(user)
