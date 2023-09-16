from app.database import Base
from sqlalchemy import Column, Integer, String


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    genres = Column(String, index=True)
    casts = Column(String, index=True)