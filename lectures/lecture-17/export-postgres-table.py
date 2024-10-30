# Ensure you have the necessary packages installed
# conda install pandas sqlalchemy psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# Replace with your actual database credentials
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

# Query the data
df = pd.read_sql_query("SELECT * FROM drivers;", engine)

# Export to CSV, change directory if necessary
os.getcwd()
df.to_csv('lectures/lecture-17/drivers.csv', index=False)