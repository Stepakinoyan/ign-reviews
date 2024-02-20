import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("id,status_code", [
    (1, 200),
    (2, 200),
    (3, 200),
    (4, 200)
])
async def test_review_by_id_api(id, status_code, ac: AsyncClient):
            
            response = await ac.post(f"/review/{id}")
            print(response.text)
            assert response.status_code == status_code