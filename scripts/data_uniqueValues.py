from pathlib import Path
import pandas as pd

base_Dir = Path.cwd().parent #Represents base directory
csv_path = base_Dir / "data" / "raw" / "rawdata_CA.csv" #Represents desired csv file

df = pd.read_csv(csv_path)

print(df['* Damage'].nunique()) #Gives total unique values in specified column name
df["* Damage"].value_counts().head() #Lists the results of specified column name

print(df['* Structure Type'].nunique()) 
df["* Structure Type"].value_counts().head() 

print(df['* City'].nunique()) 
df["* City"].value_counts().head() 

print(df['State'].nunique()) 
df["State"].value_counts().head() 

print(df['County'].nunique()) 
df["County"].value_counts().head() 

print(df['Community'].nunique()) 
df["Community"].value_counts()

print(df['* Incident Name'].nunique()) 
df["* Incident Name"].value_counts().head() 

print(df['Incident Number (e.g. CAAEU 123456)'].nunique()) 
df["Incident Number (e.g. CAAEU 123456)"].value_counts().head() 

print(df['Hazard Type'].nunique()) 
df["Hazard Type"].value_counts().head() 

print(df['* Roof Construction'].nunique()) 
df["* Roof Construction"].value_counts().head() 

print(df['* Eaves'].nunique()) 
df["* Eaves"].value_counts().head() 

print(df['* Vent Screen'].nunique()) 
df["* Vent Screen"].value_counts().head() 

print(df['* Exterior Siding'].nunique()) 
df["* Exterior Siding"].value_counts().head() 

print(df['* Window Pane'].nunique()) 
df["* Window Pane"].value_counts().head() 

print(df['* Deck/Porch on Grade'].nunique()) 
df["* Deck/Porch on Grade"].value_counts().head() 

print(df['* Deck/Porchj Elevated'].nunique()) 
df["* Deck/Porch Elevated"].value_counts().head() 

print(df['* Patio Cover/Carport Attached to Structure'].nunique()) 
df["* Patio Cover/Carport Attached to Structure"].value_counts().head() 

print(df['* Fence Attached to Structure'].nunique()) 
df["* Fence Attached to Structure"].value_counts().head() 

print(df['Distance - Propane Tank to Structure'].nunique()) 
df["Distance - Propane Tank to Structure"].value_counts().head() 

print(df['Distance - Residence to Utility/Misc Structure &gt; 120 SQFT'].nunique()) 
df["Distance - Residence to Utility/Misc Structure &gt; 120 SQFT"].value_counts().head() 

