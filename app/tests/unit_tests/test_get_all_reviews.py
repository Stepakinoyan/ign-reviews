import asyncio
from app.dao.dao import ReviewDAO


def test_get_all_reviews():
    print(asyncio.run(ReviewDAO.get_all_reviews()))