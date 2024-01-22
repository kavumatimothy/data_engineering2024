FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas psycopg2 sqlalchemy pgcli fastparquet

WORKDIR /app

ENTRYPOINT ["bash"]
