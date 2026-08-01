from pathlib import Path
import pandas as pd
import numpy as np

base_Dir = Path(__file__).parent.parent #Represents base directory
csv_path = base_Dir / "data" / "raw" / "rawdata_CA.csv" #Represents desired csv file

raw_df = pd.read_csv(csv_path, low_memory=False)
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
    .str.replace(r"[.,]", "", regex=True)
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
    "street_type_eg_road_drive_lane_etc",
    "street_suffix_eg_apt_23_blding_c",

    "state",
    "zip_code",

    "cal_fire_unit",
    "county",
    "community",
    "battalion",

    "incident_start_date",
    "incident_name",
    "incident_number_eg_caaeu_123456",

    "if_affected_where_did_fire_start",
    "if_affected_what_started_fire",
    "structure_defense_actions_taken",

    "units_in_structure_if_multi_unit",
    "of_damaged_outbuildings_lt_120_sqft",
    "of_non_damaged_outbuildings_lt_120_sqft",
    "of_damaged_or_destroyed_cars_on_property",

    "distance_propane_tank_to_structure",
    "distance_residence_to_utility_misc_structure_gt_120_sqft",

    "fire_name_secondary",
    "apn_parcel",
    "site_address_parcel",

    "year_built_parcel",
    "assessed_improved_value_parcel",

    "x",
    "y"
]

df = df.drop(columns=drop_cols)

#Standardize missing values
df = df.replace(
    ["N/A", "NA", "", "null", "NULL"], 
    np.nan
)

#Clean categorical columns
cat_cols = df.select_dtypes(include=["object", "string"]).columns

for col in cat_cols:
    df[col]= (
        df[col]
        .str.strip()
        .str.lower()
    )

clean_df = df.copy()
output_path = base_Dir / "data" / "processed" / "cleanedData_CA.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

print("\nFinal dataset shape:")
print(clean_df.shape)

print("\nFinal columns:")
print(clean_df.columns.tolist())

print("\nMissing values:")
print(clean_df.isna().sum())

clean_df.to_csv(output_path, index=False)





