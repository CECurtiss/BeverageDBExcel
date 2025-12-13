#initialize database and import excel data
#save data to database
#generate report using excel writer
from services.db_service import get_connection
from pathlib import Path

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

print("hello world")

if __name__ == "__main__":
    main()