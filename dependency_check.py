import pandas as pd
import time
import os
from google.cloud import bigquery

client = bigquery.Client()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/haobomini/Documents/github/keen-hangar-228019-6e5e2d02d2e7.json"


query_job = client.query(
    """
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10"""
)

results = query_job.result()  # Waits for job to complete.

for row in results:
    print("{} : {} views".format(row.url, row.view_count))

data1=results.to_dataframe()


def dependency_check():
    i=[1,2,3,4,5,6]
    for x in i:
        if x<5:
            print(x)
            time.sleep(5)
        else:
            print("hello")

dependency_check()

