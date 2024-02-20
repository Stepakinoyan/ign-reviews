from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel
from datetime import datetime

class FeedImage(BaseModel):
    url: str


class Contributor(BaseModel):
    name: str


class PrimaryObject(BaseModel):
    url: str


class Content(BaseModel):
    title: str
    publishDate: datetime
    feedImage: FeedImage
    url: str
    contributors: List[Contributor]

class Review(BaseModel):
    score: int


class FeedItem(BaseModel):
    content: Content
    review: Review


class ReviewContentFeed(BaseModel):
    feedItems: List[FeedItem]



class Reviews(BaseModel):
    content: Content
    review: Review
    text: str