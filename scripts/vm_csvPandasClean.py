from pathlib import Path
import pandas as pd
import numpy as np

base_Dir = Path.cwd().parent #Represents base directory
csv_path = base_Dir / "data" / "raw" / "rawdata_CA.csv" #Represents desired csv file

raw_df = pd.read_csv(csv_path)
df = raw_df.copy()

#Normalize column names
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(r"[*#?]", "", regex=True)
    .str.replace(r"[()]", "", regex=True)
    .str.replace("&gt;", "gt", regex=False)
    .str.replace(">", "gt", regex=False)
    .str.replace("<", "lt", regex=False)
    .str.replace("&", "and", regex=False)
    .str.replace(r"[\s\-\/]+", "_", regex=True)
    .str.replace(r"_+", "_", regex=True)
    .str.strip("_")
)

print(df.columns.tolist())

#Drop unncessary columns
drop_cols = [
    "objectid",
    "globalid",

    "street_number",
    "street_name",
    "street_type_(e.g._road_drive_lane_etc.)",
    "street_suffix_(e.g._apt_23_blding_c)",

    "state",
    "zip_code",

    "cal_fire_unit",
    "county",
    "community",
    "battalion",

    "incident_start_date",

    "if_affected_where_did_fire_start",
    "if_affected_what_started_fire",
    "structure_defense_actions_taken",

    "num_units_in_structure_(if_multi_unit)",
    "num_of_damaged_outbuildings_lt120_sqft",
    "num_of_non_damaged_outbuildings_lt120_sqft",
    "num_of_damaged_or_destroyed_cars_on_property",

    "distance_propane_tank_to_structure",
    "distance_residence_to_utility_misc_structure_gt_120_sqft",

    "fire_name_(secondary)",
    "apn_(parcel)",
    "site_address_(parcel)",

    "year_built_(parcel)",
    "assessed_improved_value_(parcel)",

    "x",
    "y"
]

df = df.drop(columns=drop_cols, errors="ignore")

#Standardize missing values
df = df.replace(
    ["Unknown", "N/A", "NA", "", "null", "NULL"], 
    np.nan
)

#Clean categorical columns
cat_cols = df.select_dtypes(include="object").columns

for col in cat_cols:
    df[col]= (
        df[col]
        .str.strip()
        .str.lower()
    )

clean_df = df.copy()
output_path = base_Dir / "data" / "processed" / "cleanedData_CA.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

clean_df.to_csv(output_path, index=False)





