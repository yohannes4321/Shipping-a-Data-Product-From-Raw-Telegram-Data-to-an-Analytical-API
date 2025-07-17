import psycopg2
import glob
import logging
import json
import emoji
import re

# Setup logging
logging.basicConfig(level=logging.INFO)

# Function to clean text
def remove_emojis(text):
    if text:
        text = emoji.replace_emoji(text, '')
        text = re.sub(r'\*', '', text)
        text = re.sub(r'\n', '', text)
        return text
    return text

# PostgreSQL connection
try:
    conn = psycopg2.connect(
        database='yohannes',
        user='yohannes',
        host='localhost',
        password='yohannes',
        port=5432
    )
    logging.info('Connected to PostgreSQL successfully.')
except Exception as e:
    logging.error(f'Connection failed: {e}')
    exit()

cursor = conn.cursor()

# Drop old tables
cursor.execute("DROP TABLE IF EXISTS yohannes_schema.Tellegram_data CASCADE;")
cursor.execute("DROP TABLE IF EXISTS yohannes_schema.yolo_images CASCADE;")

# Create new tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS yohannes_schema.Tellegram_data(
        message_id INT PRIMARY KEY,
        date TIMESTAMP,
        text TEXT,
        channel_name VARCHAR(256) ,
        channel_id VARCHAR(256),
        photo_path VARCHAR(256),
        product VARCHAR(256) ,
        price   TEXT 
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS yohannes_schema.yolo_images(
        message_id INT PRIMARY KEY,
        class_name VARCHAR(256),
        confidence DOUBLE PRECISION,
        photo_path VARCHAR(256) NOT NULL
    );
""")

# Process YOLO images JSON
yolo_images = glob.glob(
    'C:/Users/Hp/Documents/tenx/Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API/data/raw/telegram_messages/2025-07-17*/yolo_detected_images.json'
)

for yolo_file in yolo_images:
    with open(yolo_file, 'r', encoding='utf-8') as file:
        for line in file:
            row = json.loads(line.strip())
            cursor.execute('''
                INSERT INTO yohannes_schema.yolo_images(message_id, class_name, confidence, photo_path)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (message_id) DO NOTHING;
            ''', (
                row.get('message_id'),
                row.get('class_name'),
                row.get('confidence'),
                row.get('photo_path')
            ))

# Process Telegram messages JSON
json_files = glob.glob(
    'C:/Users/Hp/Documents/tenx/Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API/data/raw/telegram_messages/2025-07-17*/*.json'
)

logging.info(f'{len(json_files)} Telegram message JSON files found.')

for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as file:
        for line in file:
            row = json.loads(line.strip())
            cursor.execute('''
    INSERT INTO yohannes_schema.Tellegram_data(
        message_id, date, text, channel_name, channel_id, photo_path, product, price
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (message_id) DO NOTHING;
''', (
    row.get('message_id'),
    row.get('date'),
    remove_emojis(row.get('text')),
    row.get('channel_name'),
    row.get('channel_id'),
    row.get('photo_path'),
    row.get('product'),
    row.get('price')
))


# Finalize
conn.commit()
cursor.close()
conn.close()
logging.info('Data successfully saved into PostgreSQL.')
