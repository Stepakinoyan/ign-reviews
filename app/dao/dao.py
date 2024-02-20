from sqlalchemy import select
from app.database import async_session_maker
from app.news.model import News

class ReviewDAO:
    model = News

    @classmethod
    async def get_review_by_id(self, id: int):
        async with async_session_maker() as session:
            get_by_id = select(self.model.__table__.columns).filter_by(id=id)
            result = await session.execute(get_by_id)

            return result.mappings().all()
        
    @classmethod
    async def get_all_reviews(self):
        async with async_session_maker() as session:
            all_reviews = select(self.model.id, self.model.content, self.model.review)
            result = await session.execute(all_reviews)

            return result.mappings().all()