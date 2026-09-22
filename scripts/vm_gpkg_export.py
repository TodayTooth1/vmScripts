from pathlib import Path
import sqlite3
import pandas as pd

base_Dir = Path(__file__).resolve().parent.parent #Represents base directory
db_path = base_Dir / "data" / "raw" / "rawdata_CA_08.02.gpkg"
out_path = base_Dir / "data" / "processed" / "rawdataCA_cleaned.csv"

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM rawdataCA_cleaned", conn)
conn.close()

print(df.shape)
print(df.head())

df.to_csv(out_path, index=False)
print(f"Saved {len(df)} rows to {out_path}")