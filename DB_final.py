#!/usr/bin/env python3
"""
Test psycopg with CockroachDB.
"""
import pandas as pd
# df = pd.read_csv('twitter_scrape_word.csv')
# print(df.iterrows)
import logging
import os
import random
import time
import uuid
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row
# import testing


#Create table
def create_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS twitter_scrape (Tweet_id UUID PRIMARY KEY, UserScreenName VARCHAR, UserName VARCHAR, Timestamp TIMESTAMP, Text VARCHAR, Embedded_text VARCHAR, Emojis VARCHAR, Comments VARCHAR, Likes VARCHAR, Retweets VARCHAR, Image_link VARCHAR, Tweet_URL VARCHAR, Keyword VARCHAR)"
        )

#加record DF->sql db
def insert_record(conn, df):
    with conn.cursor() as cur:
        for index, arr in enumerate(df.iterrows()):
            if index ==0:
                continue
            id1 = uuid.uuid4()
            record = arr[1]
            cur.execute("UPSERT INTO twitter_scrape (tweet_id, userscreenname, username, timestamp, text, embedded_text, emojis, comments, likes, retweets, image_link, tweet_URL, keyword) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id1, record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11])
            )

#清record <all>
def delete_accounts(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM twitter_scrape")
        logging.debug("delete_twitter_scrape(): status message: %s",
                      cur.statusmessage)

#display record
def print_record(conn):
    with conn.cursor() as cur:
        print(f"record at {time.asctime()}:")
        for row in cur.execute("SELECT count(keyword) as count FROM twitter_scrape"):
            # print(row.tweet_id)
            print("count : {0}  ".format(row.count))

#delete table!!!!!!唔好亂用!!!!!!!!!!!!
def del_table(conn):
    with conn.cursor() as cur:
        cur.execute('DROP TABLE twitter_scrape')

#run function
def main():
    
    # try:
        conn = psycopg.connect("postgresql://sum:M_Fdu8h4HmN7XAWfR-jRAw@mean-grivet-3788.8nk.cockroachlabs.cloud:26257/twitter_project_red?sslmode=verify-full", 
                               application_name="$ docs_simplecrud_psycopg3", 
                               row_factory=namedtuple_row)
       
        # print('start')

        # del_table(conn)
        # delete_accounts(conn)
        # create_table(conn)
        # insert_record(conn, df)
        print_record(conn)
        conn.commit()

        # print('finish')
    # except Exception as e:
    #     logging.fatal("database connection failed")
    #     logging.fatal(e)
    #     return

#行邊個function
if __name__ == "__main__":
    main()