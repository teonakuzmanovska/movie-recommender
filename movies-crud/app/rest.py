from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import Movie, MovieCreate
from app.services import get_movies, add_movie, get_movie_by_id, search_movie_by_title,update_movie_by_id


router = APIRouter(tags=["movies"])

@router.get("/movies", response_model=list[Movie])
async def get_all_movies(db : Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return get_movies(db, offset=offset, limit=limit)

@router.post("/movies", response_model=Movie)
async def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return add_movie(db, movie)
    
@router.get("/movies/{movie_id}", response_model=Movie)
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    return get_movie_by_id(db, movie_id)

@router.patch("/movies/{movie_id}", response_model=Movie)
async def update_movie(movie_id: int, movie: MovieCreate, db: Session = Depends(get_db)):
    return update_movie_by_id(db, movie_id, movie)

@router.get("/search", response_model=list[Movie])
async def search_movie(title: str, db: Session = Depends(get_db)):
    return search_movie_by_title(db, title)