#load data into the database
import pandas as pd
from pathlib import Path
from services.db_service import DBService
from services.excel_reader import ExcelReader

class ExcelImporter(DBService):
    def __init__(self, db_path: Path):
        super().__init__(db_path)
        self.reader = ExcelReader()

    def import_df_to_db(self, excel_file: Path):
        try:
            df, table_name = self.reader.read_files(excel_file)
            conn =self.get_connection()
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"{table_name} successfully added to db.")
            conn.close()
            return df, table_name
        except Exception as e:
            print(f"Error importing data to database: {e}")
