#generate report using excel writer
import pandas as pd
from services.excel_writer import generate_xlsx_report
from services.db_service import get_connection
from pathlib import Path
from services.excel_importer import read_excel, import_excel_to_db

project_root = Path(__file__).resolve().parent
data_dir = project_root / "data"
excel_input_dir = data_dir / "excel_input"
excel_output_dir = data_dir / "excel_output"
DB_PATH = data_dir / "beverages.db"

def main():
    conn = get_connection(DB_PATH)
    if conn:
        print("Database connection established.")
    else:
        print("Failed to connect to the database.")
        #call excel importer to read and write to db
    for excel_file in excel_input_dir.glob("*.xlsx"):
        df, table_name = read_excel(excel_file)
        print(f"Tables read to dataframe: {table_name}.")
        if df is not None:
            # print(df)
            import_excel_to_db(df, table_name, conn)
        else:
            print(f"Skipping file {excel_file} due to read error.")
    generate_xlsx_report(conn, excel_output_dir / "beverage_report.xlsx")

if __name__ == "__main__":
    main()