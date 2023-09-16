from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str = None
    genres: str = None
    casts: str = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    class Config:
        orm_mode = True