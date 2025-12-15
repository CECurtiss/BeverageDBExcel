from pathlib import Path
from services.db_reader import DBReader

class ExcelWriter:
    def __init__(self, db_path: Path):
        self.db_reader = DBReader(db_path)

    def generate_xlsx_report(self, output_path: Path):
        df = self.db_reader.retrieve_from_db()
        if df is None:
            raise ValueError("No data available.")
        
        try:
        # Filter out volume_oz less than 16
            df = df[df['volume_oz'] >= 16]
            df = df.fillna({'alcohol_content': 'None'})
        
        # Write the dataframe to an xlsx file
            df.to_excel(output_path, index=False)
            print(f"Report generated successfully!")
        except Exception as e:
            raise RuntimeError(f"Failed to generate report: {e}")