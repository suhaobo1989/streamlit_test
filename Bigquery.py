import pandas as pd
import time
import os
from importlib.metadata import version
from google.cloud import bigquery ####issue with version after 3.0.0
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/haobomini/Documents/github/keen-hangar-228019-6e5e2d02d2e7.json"

###Bigquery connection
client = bigquery.Client()

query_job = client.query(
    """
    select zipcode,geo_id
from bigquery-public-data.census_bureau_usa.population_by_zip_2000
where population>100000"""
).to_dataframe()


