import schedule
import time
from DBservice import DBservice
from dataDownload import DataDownload
from ingest_config import config
from datetime import datetime

def run_tasks():
    #Download Report
    for endpoint in config["endpoints"]:
        url = endpoint["url"]    
        data_downloader = DataDownload(url)
        file_path = data_downloader.downloader()

        print("Starting Database Service")
        try:
            for each_config in config["endpoints"]:
                db_service = DBservice(database=each_config["db_name"],
                                       user=each_config["db_user"],
                                       password=each_config['db_password'],
                                       host=each_config['db_host'],
                                       port=each_config["db_port"])
                db_service.write_to_db(csv_file_path=file_path,table_name=each_config["table_name"])
            print("Ending saving in database at " + str(datetime.now()))
        except Exception as e:
            print("Failed to save data", e)

if __name__ == '__main__':
    run_tasks()
    # print("starting scheduled tasks")
    # schedule.every(12).hours.do(run_tasks)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)