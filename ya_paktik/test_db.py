#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

from sqlalchemy import create_engine

if __name__ == "__main__":   

    db_config = {'user': 'my_user',
                 'pwd': 'my_user_password',
                 'host': 'localhost',
                 'port': 5432,
                 'db': 'games'}   

    connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                             db_config['pwd'],
                                                             db_config['host'],
                                                             db_config['port'],
                                                             db_config['db'])                 

    #запрашиваем сырые данные
    engine = create_engine(connection_string)    

    query = '''
                select * from data_raw
            '''

    raw = pd.io.sql.read_sql(query, con = engine)
    print('В таблице data_raw {} записей'.format(raw.shape[0]))