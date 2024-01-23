config = {
    "endpoints":[
        {
            "url":"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz",
            "db_user":"root",
            "db_password":"root",
            "db_host":"postgres_container",
            "db_port":"5432",
            "db_name":"ny_taxi",
            "table_name":"yellow_taxi_data"
        }
    ]

}