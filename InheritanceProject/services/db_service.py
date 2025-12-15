import sqlite3
from pathlib import Path

#base class for db service
class DBService:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            print("Database connection established.")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None
