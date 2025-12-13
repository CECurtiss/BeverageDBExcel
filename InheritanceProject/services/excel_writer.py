#gets data from database and submits report of all three
import pandas as pd
from pathlib import Path

def generate_xlsx_report(conn, output_path, min_volume_oz=16):
    try:
        # Query to get requested data from all tables
        query = """
        SELECT name, volume_oz, price, alcohol_content FROM WinesTable
        UNION ALL
        SELECT name, volume_oz, price, alcohol_content FROM BeersTable
        UNION ALL
        SELECT name, volume_oz, price, alcohol_content FROM IPAsTable
        UNION ALL
        SELECT name, volume_oz, price, NULL AS alcohol_content FROM BeveragesTable
        """""
        df = pd.read_sql(query, conn)
        # Filter out volume_oz less than 16
        df = df[df['volume_oz'] >= min_volume_oz]
        
        # Write the dataframe to an xlsx file
        df.to_excel(output_path, index=False)
        print(f"Report generated successfully at {output_path}")
    except Exception as e:
        print(f"Error generating report: {e}")