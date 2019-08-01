import psycopg2
import csv
from tqdm import tqdm

#csv_data = csv.reader(file('s_okopf.csv'))

conn = psycopg2.connect(host="172.18.207.27", dbname="cases", user="dmartynov", password="LKhjkljklkwJBJjkw%499lekc$68")
cur = conn.cursor()
table_name = 'okpo_statreg_by_gleb'

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS statregistr.{}(
    okpo text,
    str_n integer,
    gr3 integer NOT NULL,
    gr4 integer NOT NULL,
    gr5 integer NOT NULL,
    gr6 text NOT NULL,
    gr7 integer NOT NULL,
    PRIMARY KEY (okpo, str_n)
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
            "INSERT INTO statregistr." + table_name + " VALUES (%s, %s, %s, %s, %s, %s, %s)", 
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
insert_into_table()
