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
        df, table_name = self.reader.read_files(excel_file)

        if df is None or table_name is None:
            raise ValueError("DataFrame or table name is None.")
        
        conn =self.get_connection()
        
        try:
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"{table_name} successfully added to db.")
            return df
        except Exception as e:
            raise RuntimeError(f"Error importing {table_name} to db: {e}")
        finally:
            conn.close()
