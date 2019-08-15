import psycopg2
import csv
import private
from tqdm import tqdm

conn = psycopg2.connect(host=private.sr_host, dbname=private.sr_dbname, user=private.sr_user, password=private.sr_password)
cur = conn.cursor()

table_name = 'test_4'
file_name = 's_status_okpo.csv'

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