from fastapi import APIRouter
from app.dao.dao import ReviewDAO

router = APIRouter(prefix="/review", tags=["Получение обзоров"])

@router.post("/catalog")
async def all_reviews():
    return await ReviewDAO.get_all_reviews()

@router.post("/{id}")
async def review_by_id(id: int):
    return await ReviewDAO.get_review_by_id(id)