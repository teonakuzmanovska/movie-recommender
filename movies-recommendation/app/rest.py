from fastapi import APIRouter
from app.services import *

router = APIRouter(tags=["recommendations"])

@router.get("/recommendations")
def get_top_recommendations():
    return get_recommendations()
