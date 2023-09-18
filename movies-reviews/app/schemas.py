from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: float = None
    comment: str = None

class ReviewCreate(ReviewBase):
    movie_id: int

# class MovieBase(BaseModel):
#     title: str
#     description: str = None
#     genres: str = None
#     casts: str = None

# class Movie(MovieBase):
#     id: int
#     class Config:
#         orm_mode = True

class Review(ReviewBase):
    id: int
    movie_id: int
    movie: dict
    class Config:
        orm_mode = True
