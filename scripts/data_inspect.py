from pathlib import Path
import pandas as pd

base_Dir = Path.cwd().parent #Represents base directory
csv_path = base_Dir / "data" / "raw" / "rawdata_CA.csv" #Represents desired csv file

df = pd.read_csv(csv_path)

df.info()
df.describe(include='all')
df.head()
df.columns
df.shape

