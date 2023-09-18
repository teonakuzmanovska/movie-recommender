# from http.client import HTTPException
# import ReviewBase
from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import Review, ReviewCreate
from app.services import get_reviews, update_review_by_id, add_review, delete_review_by_id
# import requests

router = APIRouter(tags=["reviews"])

@router.get("/reviews", response_model=list[Review])

async def get_all_reviews(db : Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return get_reviews(db, offset=offset, limit=limit)

@router.post("/reviews", response_model=Review)
def create_new_review (data: ReviewCreate , db:Session =Depends(get_db)):
    # movie_url = f"http://localhost:8000/movies-crud/movies/:id"
    # movie_response = requests.get(movie_url)
    # if movie_response.status_code != 200:
    #     raise HTTPException(status_code=404, detail="Movie not found")
    # movie = movie_response.json()
    # Review(**data.dict(), movie=movie)
    return add_review(db, data)

@router.patch("/reviews/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    return update_review_by_id(db, review_id, review)

@router.delete("/reviews/{review_id}", response_model=Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return delete_review_by_id(db, review_id)
