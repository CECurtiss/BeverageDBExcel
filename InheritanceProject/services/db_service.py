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
            raise RuntimeError(f"Failed to connect to database. {e}")
