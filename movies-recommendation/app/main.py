from fastapi import FastAPI
import uvicorn
from app.rest import router as recommendations_router
from dotenv import load_dotenv

app = FastAPI(
    title="Recommendations",
)

app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="localhost", port=8002, log_level="info")
    