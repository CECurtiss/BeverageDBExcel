#import excel files and load data into the database
import pandas as pd
from services.db_service import get_connection
from pathlib import Path

def read_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        table_name = Path(file_path).stem
        return df, table_name
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
    

def import_excel_to_db(df,table_name):
    conn = get_connection()
    if conn:
        try:
            df.to_sql(table_name, conn, if_exists='fail', index=False)
            print(f"Data imported to table {table_name} successfully.")
        except Exception as e:
            print(f"Error importing data to database: {e}")
        finally:
            conn.close()