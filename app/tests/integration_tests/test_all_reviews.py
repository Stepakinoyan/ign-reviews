from httpx import AsyncClient


async def test_get_all_reviews(ac: AsyncClient):
    get_all_reviews = await ac.post("/")
    print(get_all_reviews.text)
    assert get_all_reviews.status_code == 200
