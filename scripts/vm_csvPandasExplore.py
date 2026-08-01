from pathlib import Path
import pandas as pd
import numpy as np

base_Dir = Path(__file__).parent.parent #Represents base directory
csv_path = base_Dir / "data" / "processed" / "cleanedData_CA.csv" #Represents desired csv file

clean_df = pd.read_csv(csv_path, low_memory=False)

# Dataset overview
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print(f"Rows: {clean_df.shape[0]:,}")
print(f"Columns: {clean_df.shape[1]:,}")



# Column names
print("\n" + "=" * 50)
print("COLUMNS")
print("=" * 50)

for col in clean_df.columns:
    print(f"- {col}")


# Data types
print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)

print(clean_df.dtypes)

# Unique Values
print("\n" + "=" * 50)
print("Unqiue Values")
print("=" * 50)

clean_df["damage"].value_counts()

for col in clean_df.select_dtypes("str"):
    print(col)
    print(clean_df[col].nunique())


# Missing values
print("\n" + "=" * 50)
print("MISSING VALUES PERCENTAGE")
print("=" * 50)


missing_pct = (
    clean_df.isna()
    .mean()
    .sort_values(ascending=False)
    * 100
)

print(missing_pct)



