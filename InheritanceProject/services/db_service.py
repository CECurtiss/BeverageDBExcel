#create a database service to handle database operations
import sqlite3
from pathlib import Path

DB_PATH = Path("../data/beverages.db")

#initialize the database connection
def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
