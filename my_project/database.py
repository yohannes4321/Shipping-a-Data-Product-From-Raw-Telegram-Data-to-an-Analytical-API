import psycopg2
def get_db_connection():
    conn=psycopg2.connect(
        database='yohannes',
        user='yohannes',
        host='localhost',
        password='yohannes',
        port=5432
    )
    return conn
