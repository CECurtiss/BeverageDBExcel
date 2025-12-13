#initialize database and import excel data
#save data to database
#generate report using excel writer
from services.db_service import get_connection

def main():
    conn = get_connection()
    if conn:
        print("Database connection established.")
        conn.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()