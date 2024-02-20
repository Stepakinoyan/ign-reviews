from app.dao.dao import ReviewDAO
import asyncio
import pytest

@pytest.mark.parametrize("id", [
    (1),
    (2),
    (3)
])
def test_get_by_id(id):
    print(asyncio.run(ReviewDAO.get_review_by_id(id)))