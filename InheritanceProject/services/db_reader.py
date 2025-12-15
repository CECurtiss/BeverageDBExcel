from pathlib import Path
import pandas as pd
from services.db_service import DBService

class DBReader(DBService):
    def __init__(self, db_path: Path):
        super().__init__(db_path)

    def retrieve_from_db(self):
        conn=self.get_connection()

        try:
            query = """
            SELECT name, volume_oz, price, alcohol_content FROM BeverageList1
            UNION ALL
            SELECT name, volume_oz, price, alcohol_content FROM BeverageList2
            UNION ALL
            SELECT name, volume_oz, price, alcohol_content FROM BeverageList3
            UNION ALL
            SELECT name, volume_oz, price, alcohol_content FROM BeverageList4
            """
            df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            raise RuntimeError(f"Error retrieving data from database: {e}")
        finally:
             conn.close()