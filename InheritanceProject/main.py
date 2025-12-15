#generate report using excel writer
import pandas as pd
from services.excel_reader import ExcelReader
from services.excel_writer import generate_xlsx_report
from pathlib import Path

project_root = Path(__file__).resolve().parent
data_dir = project_root / "data"
excel_input_dir = data_dir / "excel_input"
excel_output_dir = data_dir / "excel_output"
DB_PATH = data_dir / "beverages.db"

def main():
    #read
    importer = ExcelReader()
    for excel_file in excel_input_dir.glob("*.xlsx"):
        df, table_name = importer.read_filesl(excel_file)
        print(f"Tables read to dataframe: {table_name}.")
        if df is not None:
            print(df)
            # importer.import_excel_to_db(df, table_name)
        else:
            print(f"Skipping file {excel_file} due to read error.")
    #import to db
    #generate report in xlsx format

    #For each excel file in input dir, read and import to db
    # for excel_file in excel_input_dir.glob("*.xlsx"):
    #     df, table_name = read_excel(excel_file)
    #     print(f"Tables read to dataframe: {table_name}.")
    #     if df is not None:
    #         # print(df)
    #         import_excel_to_db(df, table_name, conn)
    #     else:
    #         print(f"Skipping file {excel_file} due to read error.")
    # #Generate report using writer function
    # try:
    #     generate_xlsx_report(conn, excel_output_dir / "beverage_report.xlsx")
    # except Exception as e:
    #     print(f"Error generating report: {e}")
    # finally:
    #     conn.close()

if __name__ == "__main__":
    main()