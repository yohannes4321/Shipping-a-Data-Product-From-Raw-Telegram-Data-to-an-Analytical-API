# Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API
# Shipping a Data Product: From Raw Telegram Data to an Analytical API

An end-to-end data platform that transforms raw Telegram data into actionable business insights using modern data tools like **Telethon**, **dbt**, **YOLOv8**, **FastAPI**, and **Dagster**.

---

## 🚀 Project Overview

This project builds a data pipeline for Ethiopian medical businesses by:

- Scraping messages and images from public Telegram channels.
- Transforming and modeling the data in a PostgreSQL data warehouse using **dbt**.
- Enriching data using object detection with **YOLOv8**.
- Exposing analytical insights through an API built with **FastAPI**.
- Orchestrating the pipeline with **Dagster**.

---

## 📊 Business Questions Answered

- Top 10 most mentioned medical products or drugs.
- Price or availability of specific products across channels.
- Channels with the most visual content (images).
- Daily and weekly posting trends for health topics.

---

## 🛠️ Technologies Used

- **Python** (v3.x)
- **Docker** & **docker-compose**
- **PostgreSQL**
- **Telethon** (Telegram scraping)
- **YOLOv8** (Object detection)
- **dbt** (Data modeling & transformation)
- **FastAPI** (Analytical API)
- **Dagster** (Pipeline orchestration)

---

## 📂 Project Structure

my_project/
├── data/
│ └── raw/telegram_messages/YYYY-MM-DD/channel_name.json
├── dags/ # Dagster jobs and pipelines
├── dbt/ # dbt project for transformations
├── images/ # Scraped images for YOLO processing
├── api/ # FastAPI app
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ └── crud.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env # Secrets (not committed)
└── README.md


---

## 🔑 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yohannes4321/Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API.git
cd Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API

2. Environment Setup

    Define secrets in .env (Telegram API keys, DB credentials).

    Install Python dependencies:

pip install -r requirements.txt

    Alternatively, use Docker:

docker-compose up --build

📥 Data Collection (Task 1)

    Scrape messages and images from:

        Lobelia Cosmetics

        Tikvah Pharma

        Other channels listed on et.tgstat.com/medicine.

    Raw data stored as JSON files.

📊 Data Modeling & Transformation (Task 2)

    Load raw data into PostgreSQL.

    Use dbt to:

        Clean and transform data.

        Create star schema:

            dim_channels

            dim_dates

            fct_messages

    Run dbt models:

dbt run

    Validate models:

dbt test

🖼️ Data Enrichment (Task 3)

    Use YOLOv8 for image analysis:

from ultralytics import YOLO
model = YOLO('yolov8n.pt')

    Enrich data with detected objects and store in fct_image_detections.

📡 Analytical API (Task 4)

    API endpoints (examples):

        /api/reports/top-products?limit=10

        /api/channels/{channel_name}/activity

        /api/search/messages?query=paracetamol

    Run FastAPI:

uvicorn api.main:app --reload

📅 Pipeline Orchestration (Task 5)

    Use Dagster for running and scheduling the pipeline:

dagster dev

    Define jobs:

        scrape_telegram_data

        load_raw_to_postgres

        run_dbt_transformations

        run_yolo_enrichment

📈 Reports & Documentation

    dbt Docs:

dbt docs generate
dbt docs serve

    Include:

        Star schema diagram.

        Pipeline architecture diagram.

        Screenshots of API responses.

📃 License

Project developed by Kara Solutions for educational and analytical purposes.
🔗 Useful References

    Telethon Docs

    dbt Documentation

    Ultralytics YOLOv8 Docs

    FastAPI Documentation

    Dagster Documentation


---

Let me know if you'd like this README customized for your personal GitHub profile 
