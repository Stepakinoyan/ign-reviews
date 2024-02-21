from sqlalchemy import delete, insert, select
from app.news.news_parser import reviews
from app.tasks.celery import celery
from asgiref.sync import async_to_sync
from app.news.model import News
from app.database import async_session_maker

async def drop_db():
        async with async_session_maker() as session:
                drop = delete(News)
                await session.execute(drop)

                await session.commit()

async def prepare_db():
        async with async_session_maker() as session:
                await drop_db()
                query = insert(News).values(reviews.return_all_reviews())
                await session.execute(query)

                await session.commit()

@celery.task(name="prepare_db_every_day")
def prepare_db_task():
        async_to_sync(prepare_db)()