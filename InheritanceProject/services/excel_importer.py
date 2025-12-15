#import excel files and load data into the database
import pandas as pd
from pathlib import Path


    

def import_excel_to_db(df,table_name, conn):
        try:
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"Data imported to table {table_name} successfully.")
        except Exception as e:
            print(f"Error importing data to database: {e}")
