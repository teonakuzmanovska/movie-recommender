# from http.client import HTTPException
# import ReviewBase
from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import Review, ReviewCreate
from app.services import get_reviews, update_review_by_id, add_review, delete_review_by_id
# from app.keycloak import authenticate_keycloak  # Import the authentication function
# import requests
from fastapi.security.oauth2 import OAuth2PasswordBearer
from app.settings import KEYCLOAK_SERVER_URL

router = APIRouter(tags=["reviews"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{KEYCLOAK_SERVER_URL}/protocol/openid-connect/token")

@router.get("/reviews", response_model=list[Review])
async def get_all_reviews(db : Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return get_reviews(db, offset=offset, limit=limit)

@router.post("/reviews", response_model=Review)
def create_new_review (data: ReviewCreate , db:Session = Depends(get_db), current_user: dict = Depends(oauth2_scheme)):
    return add_review(db, data)

@router.patch("/reviews/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewCreate, db: Session = Depends(get_db), current_user: dict = Depends(oauth2_scheme)):
    return update_review_by_id(db, review_id, review)

@router.delete("/reviews/{review_id}", response_model=Review)
def delete_review(review_id: int, db: Session = Depends(get_db), current_user: dict = Depends(oauth2_scheme)):
    return delete_review_by_id(db, review_id)
