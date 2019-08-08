import psycopg2
import csv
from tqdm import tqdm

conn = psycopg2.connect(host="172.18.207.27", dbname="cases", user="dmartynov", password="LKhjkljklkwJBJjkw%499lekc$68")
cur = conn.cursor()
table_name = 'test_3'
file_name = ''

def create_table_with_csvheader():
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        csv_header = next(csv_reader)
        header_to_insert = ''
        for i in csv_header:      
            header_to_insert = header_to_insert+ (i + ' text NOT NULL,')
        header_to_insert = header_to_insert[0:-1]
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS statregistr.{table_name}(
        {header_to_insert}
        )
        """)
        conn.commit()
        print(f"{table_name} created successfully")
#cur.execute("select * from statregistr.s_okfs;")
#for record in cur:
#    print(record)
def insert_into_table():
    with open(file_name, 'r') as f:
        cur.copy_expert(f'COPY statregistr.{table_name} FROM STDIN WITH CSV HEADER', f)
    conn.commit()
    print('Inserted successfully')

create_table_with_csvheader()
insert_into_table()