from database import get_db_connection
def get_top_products(limit=10):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(f"""
    SELECT product,COUNT(*) AS mentions
    from yohannes_schema.fct_message
    group by product
    order by mentions DESC
    LIMIT {limit};

""")
    res=cursor.fetchall()
    cursor.close()
    conn.close()
    return res
def get_channel_activity(channel_name):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(f"""
    SELECT date:date ,COUNT(*)
    from yohannes_schema.fct_message
    WHERE channel_name =%s
    GROUP BY date:: date
    Order BY date :: date;


""",(channel_name,))
    res=cursor.fetchall()
    cursor.close()
    conn.close()
    return res
def search_messages(keyword):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT message_id, text, product, channel_name
        FROM yohannes_schema.fct_message
        WHERE text ILIKE %s
        ORDER BY date DESC
        LIMIT 100;
    """, (f"%{keyword}%",))
    results = cur.fetchall()
    conn.close()
    return results