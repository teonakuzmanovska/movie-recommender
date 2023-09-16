from fastapi import FastAPI
import uvicorn
from app.rest import router as movies_router
from app.database import Base, engine
from dotenv import load_dotenv

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movies CRUD",
)


app.include_router(movies_router, prefix="/movies-crud", tags=["movies"])

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="localhost", port=8000, log_level="info")