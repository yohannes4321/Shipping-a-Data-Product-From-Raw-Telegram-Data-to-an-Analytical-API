from fastapi import FastAPI
from typing import List
from crud import get_top_products, get_channel_activity, search_messages
from schemas import ProductReport, ChannelActivity, SearchMessage

app = FastAPI(title="Telegram Analytical API")


@app.get("/api/reports/top-products", response_model=List[ProductReport])
def top_products(limit: int = 10):
    products = get_top_products(limit)
    return [{"product": p, "mentions": c} for p, c in products]


@app.get("/api/channels/{channel_name}/activity", response_model=List[ChannelActivity])
def channel_activity(channel_name: str):
    activity = get_channel_activity(channel_name)
    return [{"date": str(d), "message_count": count} for d, count in activity]


@app.get("/api/search/messages", response_model=List[SearchMessage])
def search_messages_api(query: str):
    messages = search_messages(query)
    return [
        {
            "message_id": mid,
            "text": text,
            "product": product,
            "channel_name": channel
        }
        for mid, text, product, channel in messages
    ]
