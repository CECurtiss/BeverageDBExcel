from pathlib import Path
import pandas as pd

class ExcelReader:
    def read_files(self, file_path: Path):
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} does not exist.")
        if file_path.suffix != ".xlsx":
            raise ValueError("File is not of type .xlsx.")
        
        try:
            df = pd.read_excel(file_path)
            table_name = Path(file_path).stem
            # print(df)
            return df, table_name
        except Exception as e:
            raise RuntimeError(f'Failed to read {file_path}: {e}')

         