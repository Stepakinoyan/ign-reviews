from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

class News(Base):
        __tablename__ = 'news'
        
        id: Mapped[int] = mapped_column(primary_key=True)
        content: Mapped[list[str]] = mapped_column(JSON)
        review: Mapped[list[str]] = mapped_column(JSON)
        text: Mapped[str] = mapped_column()