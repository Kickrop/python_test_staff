import psycopg2
import csv
from tqdm import tqdm

#csv_data = csv.reader(file('s_okopf.csv'))

conn = psycopg2.connect(host="172.18.207.27", dbname="cases", user="dmartynov", password="LKhjkljklkwJBJjkw%499lekc$68")
cur = conn.cursor()
table_name = 'razdel_1_2_1'

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS statregistr.{}(
    okpo text PRIMARY KEY,
    okved_main_reg text,
    okved_main_fact text,
    okato_reg text,
    okato_fact text,
    oktmo_reg text,
    oktmo_fact text,
    okfs text,
    okogu text,
    okopf text,
    org_type integer,
    org_ovz text,
    org_status text,
    org_sost text,
    org_izm text,
    predpr_type text,
    registr_date date,
    registr_date_s text,
    inn text,
    ogrn text,
    kpp text,
    web text,
    tel text,
    fax text,
    mail text,
    okpo_head text
    )
    """.format(table_name))
    conn.commit()
    print("Table created")
def insert_into_table():
    with open('razdel_1_1.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in tqdm(reader):
            #print(row)
            cur.execute(
            "INSERT INTO statregistr.{} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(table_name),
            row
            )
    conn.commit()
    print('Inserted')
#def insert_into_table():
#    with open('s_okopf.csv', 'r') as f:
#        next(f)
#        cur.copy_from(f, 'statregistr.s_okopf', sep=';')
#    conn.commit()
#create_table()
insert_into_table()
