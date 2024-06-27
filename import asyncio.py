import asyncio
from pyppeteer import launch
import csv
import pandas as pd
import re
from datetime import date
import os
from google.cloud import bigquery
import pyodbc
from sqlalchemy import create_engine
import psycopg2

### send data to Azure
# Azure SQL Database connection details
server = 'haobo.database.windows.net'
database = 'haobo'
username = 'CloudSAb4ee53f1'
password = 'Shb3388069!'

# Create SQLAlchemy engine
connection_string = (
    "mssql+pyodbc://CloudSAb4ee53f1:Shb3388069!@haobo.database.windows.net/haobo?driver={SQL Server}"
)
engine = create_engine(connection_string, echo=False)