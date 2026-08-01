
# Branch: 02_projectformat

### Date: 28/06/2026

RangeIndex: 132522 entries, 0 to 132521
Data columns (total 47 columns):

# Column                                                        Non-Null Count   Dtype  

---  ------                                                        --------------   -----  
 0   OBJECTID                                                      132522 non-null  int64  
 1   GLOBALID                                                      132522 non-null  str    
 2   *Damage                                                      132522 non-null  str     
 3* Structure Type                                              132522 non-null  str       
 4   *Street Number                                               128102 non-null  float64  
 5* Street Name                                                 127033 non-null  str
 6   *Street Type (e.g. road, drive, lane, etc.)                  117928 non-null  str
 7   Street Suffix (e.g. apt. 23, blding C)                        63094 non-null   str
 8* City                                                        100179 non-null  str
 9   State                                                         132515 non-null  str
 10  Zip Code                                                      79722 non-null   float64
 11  *CAL FIRE Unit                                               132522 non-null  str
 12  County                                                        132492 non-null  str
 13  Community                                                     54866 non-null   str
 14  Battalion                                                     6785 non-null    object
 15* Incident Name                                               132522 non-null  str
 16  Incident Number (e.g. CAAEU 123456)                           132522 non-null  str
 17  Incident Start Date                                           132522 non-null  str
 18  Hazard Type                                                   132522 non-null  str
 19  If Affected - Where did fire start?                           12400 non-null   str
 20  If Affected - What started fire?                              10676 non-null   str
 21  Structure Defense Actions Taken                               36169 non-null   str
 22  Structure Category                                            132522 non-null  str
 23  # Units in Structure (if multi unit)                          61929 non-null   float64
 24  # of Damaged Outbuildings < 120 SQFT                          61939 non-null   float64
 25  # of Non Damaged Outbuildings < 120 SQFT                      61958 non-null   float64
 26  # of Damaged or Destroyed Cars on Property                    56188 non-null   float64
 27  *Roof Construction                                           131895 non-null  str
 28* Eaves                                                       131411 non-null  str
 29  *Vent Screen                                                 131325 non-null  str
 30* Exterior Siding                                             131614 non-null  str
 31  *Window Pane                                                 131547 non-null  str
 32* Deck/Porch On Grade                                         132522 non-null  str
 33  *Deck/Porch Elevated                                         132522 non-null  str
 34* Patio Cover/Carport Attached to Structure                   132521 non-null  str
 35  * Fence Attached to Structure                                 110928 non-null  str
 36  Distance - Propane Tank to Structure                          24005 non-null   str
 37  Distance - Residence to Utility/Misc Structure &gt; 120 SQFT  19016 non-null   str
 38  Fire Name (Secondary)                                         21171 non-null   str
 39  APN (parcel)                                                  131870 non-null  object
 40  Assessed Improved Value (parcel)                              126482 non-null  float64
 41  Year Built (parcel)                                           102091 non-null  float64
 42  Site Address (parcel)                                         127193 non-null  str
 43  Latitude                                                      132522 non-null  float64
 44  Longitude                                                     132522 non-null  float64
 45  x                                                             132522 non-null  float64
 46  y                                                             132522 non-null  float64
dtypes: float64(12), int64(1), object(2), str(32)

(132522, 47)

# Unique Values In Columns

##### Damage

* Damage
Destroyed (>50%)     70390
No Damage            54414
Affected (>0-10%)     5057
Minor (10-25%)        1356
Major (25-50%)         714
Name: count, dtype: int64

##### Structure Type

* Structure Type
Single Family Residence Single Story    47272
Utility Misc Structure                  35871
Single Family Residence Multi Story     28386
Mobile Home Double Wide                  6262
Commercial Building Single Story         3867
Name: count, dtype: int64

# Crap

categorical_columns = [
    "*Damage",
    "* Structure Type",
    "*City",
    "County",
    "Community",
    "* Incident Name",
    "Incident Number (e.g. CAAEU 123456)",
    "Hazard Type",
    "*Roof Construction",
    "* Eaves",
    "*Vent Screen",
    "* Exterior Siding",
    "*Window Pane",
    "* Deck/Porch on Grade",
    "*Deck/Porch Elevated",
    "* Patio Cover/Carport Attached to Structure",
    "* Fence Attached to Structure",
    "Distance - Propane Tank to Structure",
    "Distance - Residence to Utility/Misc Structure &gt; 120 SQFT",
]

with open("unique_values.md", "w", encoding="utf-8") as f:
    f.write("# Dataset Unique Values \n\n")

    for col in categorical_columns:
        f.write(f"## {col}\n\n")

    if col in df.columns:
        values = (
            df[col]
            .dropna()
            .astype(str)
            .sort_values()
            .unique()
            )

    counts = df[col].value_counts(dropna=False)

    f.write("| Value | Count |\n")
    f.write("|------|------|\n")

    for value, count in counts.items():
        f.write(f" | {value} | {count} | \n")
        f.write("\n---\n\n")

df_camp = df[df['* Incident Name'] == icdn] #Set's filtered view

df_camp.to_csv("camp_fire_structures.csv", index=False) #Exports filtered view
