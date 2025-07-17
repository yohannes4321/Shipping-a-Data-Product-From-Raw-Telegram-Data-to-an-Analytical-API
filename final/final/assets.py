from dagster import job,op
import subprocess

@op
def scrape_tellegram_data():
    subprocess.run(["python","tellegram_copy.py"],check=True)
@op
def load_raw_to_postgress():
    subprocess.run(["python","loading_json_postgress.py"],check=True)
@op
def run_yolo_enrichment():
    subprocess.run(['python','Yolo_image_detection.py'],check=True)
@op
def run_dbt():
    subprocess.run(['python','dbt run'])


@job
def telegram_pipline():
    scrape_tellegram_data()
    run_yolo_enrichment()
    load_raw_to_postgress()
    run_dbt()
