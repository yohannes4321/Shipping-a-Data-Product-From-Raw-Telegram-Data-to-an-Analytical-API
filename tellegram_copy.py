import logging
from telethon import TelegramClient
from load_dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
from datetime import datetime

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
client = TelegramClient('anon', api_id, api_hash)

import re


known_products = [
    "Mela-One",
    "Azithromycin",
    "CVS Daytime",
    "Omeprazole",
    "Sildenafil",
    "Captopril",
    "Ciprofloxacin",
    "Doxycycline",
    "Captopril",
    "Ampicillin",
    "Ciprofloxacin",
    "Doxycycline",
    "Levothyroxine",
    "Iron supplement",
    "Paracetamol",
    "CVS Daytime & Nighttime Cold and Flu Relief"
]

def extract_product(text):
    found_products = []  # Always define this first
    
    if isinstance(text, str) and text.strip():
        for product in known_products:
            pattern = re.compile(rf"\b{re.escape(product)}\b", re.IGNORECASE)
            if pattern.search(text):
                found_products.append(product)
                
    return found_products

def extract_price(text):
    if isinstance(text, str) and text.strip():
        pattern = re.compile(r"(\d{2,7})\s*(birr|Br|ETB|ብር)", re.IGNORECASE)
        matches = pattern.findall(text)
        return [f"{amount} {currency}" for amount, currency in matches]
    return []



async def main():
    today = datetime.now()
    today_str = today.strftime('%Y-%m-%d')
    
    channels = ['https://t.me/CheMed123', 'https://t.me/lobelia4cosmetics', 'https://t.me/tikvahpharma']

    for ch in channels:
       
        channel_name = ch.split('/')[-1]
        messages_data = []  # Collect all messages
        dir_path = f"data/raw/telegram_messages/{today_str}/{channel_name}"
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f'Data will be saved to {dir_path}')
        async for message in client.iter_messages(channel_name, limit=60):
            text = message.text if message.text else None
            path = None
            if message.photo:
                path = await message.download_media(file=dir_path)
                if path:
                    path = path.replace('\\', '/')  # Clean path for JSON
                logging.info(f'Downloaded media from {channel_name}: {path}')

            messages_data.append({
                'message_id': message.id,
                'date': str(message.date),
                'text': text,
                'channel_name': channel_name,
                'channel_id': ch,
                'product': extract_product(text),
                'price':extract_price(text),

                'photo_path': path
            })

        # Save once per channel after collecting all messages
        df = pd.DataFrame(messages_data)
        json_path = f'{dir_path}.json'
        df.to_json(json_path, orient='records', lines=True, force_ascii=False)
        logging.info(f'Saved {len(messages_data)} messages from {channel_name} to {json_path}')


# Connect and run
with client:
    client.loop.run_until_complete(main())
    logging.info('Client is running')
