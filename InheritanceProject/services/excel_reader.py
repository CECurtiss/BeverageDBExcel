from pathlib import Path
import pandas as pd

class ExcelReader:
    def read_files(self, file_path: Path):
        try:
            df = pd.read_excel(file_path)
            table_name = Path(file_path).stem
            # print(df)
            return df, table_name
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

         