#gets data from database and submits report of all three
import pandas as pd

def generate_xlsx_report(conn, output_path):
    try:
        # Query to get requested data from all tables
        query = """
        SELECT name, volume_oz, price, alcohol_content FROM BeverageList1
        UNION ALL
        SELECT name, volume_oz, price, alcohol_content FROM BeverageList2
        UNION ALL
        SELECT name, volume_oz, price, alcohol_content FROM BeverageList3
        UNION ALL
        SELECT name, volume_oz, price, alcohol_content FROM BeverageList4
        """""
        df = pd.read_sql(query, conn)
        # Filter out volume_oz less than 16
        df = df[df['volume_oz'] >= 16]
        df = df.fillna({'alcohol_content': 'None'})
        
        # Write the dataframe to an xlsx file
        df.to_excel(output_path, index=False)
        print(f"Report generated successfully at {output_path}")
    except Exception as e:
        print(f"Error generating report: {e}")