import urllib.request
import os

import pandas as pd


class DataDownload:
    def __init__(self, url: str):
        self.__url = url

    def downloader(self):
        if self.__url.endswith('.csv.gz'):
            csv_name = 'output.csv.gz'
        else:
            csv_name = 'output.csv'

        try:
            print("Downloading csv-file")
            urllib.request.urlretrieve(self.__url, csv_name)
            # os.system(f"wget {self.__url} -O {csv_name}")
            print("Data downloaded successfully")
            container_filepath = os.path.abspath(csv_name)
            print(f'{container_filepath}')
            return container_filepath
        except Exception as e:
            print("Failed to download report", e)


