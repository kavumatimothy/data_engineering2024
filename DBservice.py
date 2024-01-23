import pandas as pd
from time import time
from sqlalchemy import create_engine

class DBservice:
    def __init__(self, database: str,
                 user: str,
                 password: str,
                 host: str,
                 port: int):
        self.__database = database
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port

    def write_to_db(self, table_name: str, csv_file_path):

        # establish connections
        engine = create_engine(f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/'
                               f'{self.__database}')

        print("connection established successfully")

        df_iter = pd.read_csv(csv_file_path, iterator=True, chunksize=100000)

        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        print(f'{df.head()}')

        df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
        print(f'created {table_name} table successfully')

        df.to_sql(name=table_name, con=engine, if_exists='append')
        print('loaded first chunk')

        while True:
            try:
                t_start = time()
                df = next(df_iter)

                df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
                df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

                df.to_sql(name=table_name, con=engine, if_exists='append')

                t_end = time()
                print('Inserted another chunk, took %.3f seconds' % (t_end - t_start))

            except StopIteration:
                print("Finished ingesting data into the postgres database")
                break

