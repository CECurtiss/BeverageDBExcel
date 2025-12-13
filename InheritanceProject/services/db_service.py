#create a database service to handle database operations
import sqlite3
from pathlib import Path

#initialize the database connection
def get_connection(db_path: Path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
