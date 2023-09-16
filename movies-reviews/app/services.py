from app.models import Review
from sqlalchemy.orm import Session

def get_reviews(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Review).offset(offset).limit(limit).all()

def add_review(db: Session, review):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review_by_id(db: Session, review_id: int, review):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    db_review.comment = review.comment
    db_review.rating = review.rating
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review_by_id(db: Session, review_id: int):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    db.delete(db_review)
    db.commit()
    return db_review
