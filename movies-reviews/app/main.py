from fastapi import FastAPI
import uvicorn
from app.rest import router as reviews_router
from app.database import Base, engine
from dotenv import load_dotenv

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reviews",
)

app.include_router(reviews_router, prefix="/movies-reviews", tags=["reviews"])

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="localhost", port=8001, log_level="info")
    