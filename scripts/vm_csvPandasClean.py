from pathlib import Path
import pandas as pd

csv_path = Path(r"C:\Users\rming\Documents\GitHub\vmScripts\data\postfire_scripted.csv")

df = pd.read_csv(csv_path)

print(df['* Incident Name'].nunique()) #Gives total unique values in specified column name

df["* Incident Name"].value_counts().head(20) #Lists the 20 top results of specified column name


icdn = "Camp" #Set incident name

df_camp = df[df['* Incident Name'] == icdn] #Set's filtered view

df_camp.to_csv("camp_fire_structures.csv", index=False) #Exports filtered view



