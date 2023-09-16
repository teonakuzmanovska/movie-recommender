from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, index=True)
    rating = Column(Float)
    comment = Column(Text)

    # Define a relationship with the User and Movie models
    # movie = relationship("Movie", back_populates="reviews")
