import psycopg2
import csv
from tqdm import tqdm

#csv_data = csv.reader(file('s_okopf.csv'))

conn = psycopg2.connect(host="172.18.207.27", dbname="cases", user="dmartynov", password="LKhjkljklkwJBJjkw%499lekc$68")
cur = conn.cursor()
table_name = ''

cur.execute("select * from statregistr.s_okfs;")
for record in cur:
    print(record)

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS statregistr.{}(
    id serial,
    test1 text NOT NULL,
    name text NOT NULL
    )
    """.format(table_name))
    conn.commit()
    print("{} created successfully".format(table_name))
def insert_into_table():
    with open(table_name + '.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in tqdm(reader):
            #print(row)
            cur.execute(
            "INSERT INTO statregistr." + table_name + " VALUES (%s, %s)", 
            row
            #"INSERT INTO statregistr.{} VALUES ({})".format(table_name,row) 
            )
    conn.commit()
    print('Inserted successfully')
#def insert_into_table():
#    with open('s_okopf.csv', 'r') as f:
#        next(f)
#        cur.copy_from(f, 'statregistr.s_okopf', sep=';')
#    conn.commit()
#create_table()
#insert_into_table()
