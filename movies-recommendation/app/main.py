from fastapi import FastAPI
import uvicorn
from app.rest import router as recommendations_router
from dotenv import load_dotenv

app = FastAPI(
    title="Recommendations",
    openapi_url="/openapi.json",  # URL where OpenAPI JSON will be served
    docs_url="/docs",
)

app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="localhost", port=8005, log_level="info")
    