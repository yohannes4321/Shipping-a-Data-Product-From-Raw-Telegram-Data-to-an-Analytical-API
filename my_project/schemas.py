from pydantic import BaseModel
from typing import List


class ProductReport(BaseModel):
    product: str
    mentions: int


class ChannelActivity(BaseModel):
    date: str
    message_count: int


class SearchMessage(BaseModel):
    message_id: int
    text: str
    product: str
    channel_name: str
