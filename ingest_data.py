#!/usr/bin/env python
# coding: utf-8

# In[1]:

from time import time
import pandas as pd

file_path = 'C:/Datatalks/yellow_tripdata_2021-01.csv'
df = pd.read_csv(file_path)

print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))

from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

engine.connect()

print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

df_iter = pd.read_csv(file_path, iterator=True, chunksize=100000)

df = next(df_iter)

df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

while True:
    t_start = time()
    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

    t_end = time()

    print('inserted another chunck ....%.03f' % (t_end - t_start))

# In[ ]:




