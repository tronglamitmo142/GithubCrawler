import json
from sqlite3 import DatabaseError 
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



DATABASE_CONFIG = {
    'dbname': 'postgres',
    'user': 'nguyenlam',
    'password': 'zxcvbnm@12345',
    'host': 'localhost'
}

def get_connection():
    return psycopg2.connect(
        database = DATABASE_CONFIG.get('dbname'),
        user = DATABASE_CONFIG.get('user'),
        password  = DATABASE_CONFIG.get('password'),
        host = DATABASE_CONFIG.get('host'),
    )


def insert_value(data, conn):
    curr = conn.cursor()
    curr.execute("""
    create table if not exists json_data_table(
        repoFullName text, url text, owner text, description text, language text
    ) """)
    query_sql = """
    insert into json_data_table
        select * from json_populate_recordset(NULL::json_data_table, %s)
    """
    curr.execute(query_sql, (json.dumps(data),))
    conn.commit()


def main():
    conn = get_connection()
    with open('data.json') as f:
        data = json.load(f)
        insert_value(data=data, conn=conn)

if __name__ == '__main__':
    main()

