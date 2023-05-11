import psycopg2
from psycopg2 import sql

def create_user(name, email, password_hash):
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
        dbname=os.getenv('POSTGRES_DATABASE'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    cur = conn.cursor()

    insert = sql.SQL(
        "INSERT INTO User (name, email, password_hash) VALUES (%s, %s, %s)"
    )
    values = (name, email, password_hash)

    cur.execute(insert, values)
    conn.commit()

    cur.close()
    conn.close()
