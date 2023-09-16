
from app.models import Movie
from sqlalchemy.orm import Session

def get_movies(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Movie).offset(offset).limit(limit).all()

def add_movie(db: Session, movie):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def update_movie_by_id(db: Session, movie_id: int, movie):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db_movie.title = movie.title
    db_movie.description = movie.description
    db_movie.genres = movie.genres
    db_movie.casts = movie.casts
    db.commit()
    db.refresh(db_movie)
    return db_movie
    
def search_movie_by_title(db: Session, title: str):
    return db.query(Movie).filter(Movie.title.contains(title)).all()