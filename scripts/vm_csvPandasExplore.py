from pathlib import Path
import pandas as pd

base_Dir = Path(__file__).resolve().parent.parent
csv_path = base_Dir / "data" / "processed" / "rawdataCA_cleaned.csv"

df = pd.read_csv(csv_path)

print(df.shape)
print(df.info())

print(df['fence_attached_to_structure'].value_counts(dropna=False))

df['fence_missing'] = df['fence_attached_to_structure'].isna()

print(pd.crosstab(df['damage'], df['fence_missing']))

missing_rate = df.groupby('damage')['fence_missing'].mean()
print(missing_rate)