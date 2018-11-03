#!/usr/bin/python
import json

import psycopg2
import requests

from config import config, youtube


def get_data():
    url = "https://www.googleapis.com/youtube/v3/videos"
    parameters = {'part': 'statistics',
                  'id': 'c7rCyll5AeY',
                  'key': youtube()['key']}
    r = requests.get(url=url, params=parameters)
    data = r.json()
    print(data)
    return data


def connect(input):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version();')
        cur.execute('create table if not exists videos (payload jsonb);')
        cur.execute(f"insert into videos values {json.dumps(input)}")
        cur.execute('select * from videos;')

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    input = get_data()
    connect(input)
