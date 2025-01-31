import psycopg2
from config import DATABASE_CONFIG

def load_data(data):
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    
    for index, row in data.iterrows():
        cur.execute("""
            INSERT INTO sales (product, quantity, price, total)
            VALUES (%s, %s, %s, %s)
            """, (row['product'], row['quantity'], row['price'], row['total']))
    
    conn.commit()
    cur.close()
    conn.close()
