#generate report using excel writer
from services.excel_importer import ExcelImporter
from services.excel_writer import ExcelWriter
from pathlib import Path

project_root = Path(__file__).resolve().parent
data_dir = project_root / "data"
excel_input_dir = data_dir / "excel_input"
excel_output_dir = data_dir / "excel_output"
DB_PATH = data_dir / "beverages.db"

def main():
    #read and import to db
    importer = ExcelImporter(DB_PATH)
    for excel_file in excel_input_dir.glob("*.xlsx"):
        df = importer.import_df_to_db(excel_file)
        if df is not None:
            print(df)
        else:
            print(f"Skipping file {excel_file} due to read error.")
    

    #generate report in xlsx format
    writer = ExcelWriter(DB_PATH)
    output_file = excel_output_dir / "BeverageReport.xlsx"
    writer.generate_xlsx_report(output_file)


if __name__ == "__main__":
    main()