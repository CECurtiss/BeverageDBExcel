#create a database service to handle database operations
import sqlite3
import pandas as pd

DB_PATH = "../data/beverages.db"

#initialize the database connection
def init_db(DB_PATH):
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
