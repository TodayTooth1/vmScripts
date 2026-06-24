# 06/23/2026 Notes:

DtypeWarning: Columns (0: Battalion, 1: Fire Name (Secondary), 2: APN (parcel)) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv(csv_path)
(132522, 47)
<class 'pandas.DataFrame'>
RangeIndex: 132522 entries, 0 to 132521
Data columns (total 47 columns):
 #   Column                                                        Non-Null Count   Dtype  
---  ------                                                        --------------   -----  
 0   OBJECTID                                                      132522 non-null  int64  
 1   GLOBALID                                                      132522 non-null  str    
 2   * Damage                                                      132522 non-null  str    
 3   * Structure Type                                              132522 non-null  str    
 4   * Street Number                                               128102 non-null  float64
 5   * Street Name                                                 127033 non-null  str    
 6   * Street Type (e.g. road, drive, lane, etc.)                  117928 non-null  str    
 7   Street Suffix (e.g. apt. 23, blding C)                        63094 non-null   str    
 8   * City                                                        100179 non-null  str    
 9   State                                                         132515 non-null  str    
 10  Zip Code                                                      79722 non-null   float64
 11  * CAL FIRE Unit                                               132522 non-null  str    
 12  County                                                        132492 non-null  str    
 13  Community                                                     54866 non-null   str    
 14  Battalion                                                     6785 non-null    object 
 15  * Incident Name                                               132522 non-null  str    
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
 27  * Roof Construction                                           131895 non-null  str    
 28  * Eaves                                                       131411 non-null  str    
 29  * Vent Screen                                                 131325 non-null  str    
 30  * Exterior Siding                                             131614 non-null  str    
 31  * Window Pane                                                 131547 non-null  str    
 32  * Deck/Porch On Grade                                         132522 non-null  str    
 33  * Deck/Porch Elevated                                         132522 non-null  str    
 34  * Patio Cover/Carport Attached to Structure                   132521 non-null  str    
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
memory usage: 47.5+ MB
None
   OBJECTID                              GLOBALID           * Damage                      * Structure Type  * Street Number  * Street Name  ... Year Built (parcel)                    Site Address (parcel)   Latitude   Longitude              x             y
0    175887  9de99d4a-93c0-4a92-882f-394a95a2ba2d          No Damage   Single Family Residence Multi Story           8376.0   Quail Canyon  ...              1997.0  8376 QUAIL CANYON RD VACAVILLE CA 95688  38.474960 -122.044465 -178141.976806  52899.580457
1    175888  3810a17f-fb11-40aa-b0b8-639462bbdc99  Affected (>0-10%)  Single Family Residence Single Story           8402.0   Quail Canyon  ...              1980.0  8402 QUAIL CANYON RD VACAVILLE CA 95688  38.477442 -122.043252 -178030.386869  53173.077895
2    175889  6424dc94-71ea-48d2-a256-e12678a79563          No Damage  Single Family Residence Single Story           8430.0  Quail Canyon   ...              2004.0  8430 QUAIL CANYON RD VACAVILLE CA 95688  38.479358 -122.044585 -178141.853342  53388.500303
3    175890  2e93c136-78a6-4135-a1cf-96a27fcac854          No Damage  Single Family Residence Single Story           3838.0    Putah Creek  ...              1981.0     3838 PUTAH CREEK RD WINTERS CA 95694  38.487313 -122.015115 -175555.827392  54217.683593
4    175891  391ac3dc-5730-4120-8c5c-e936d15c82ee          No Damage  Single Family Residence Single Story           3830.0    Putah Creek  ...              1980.0     3830 PUTAH CREEK RD WINTERS CA 95694  38.485636 -122.016122 -175644.839150  54023.816111

[5 rows x 47 columns]

# Known Structure Total:
23,628

### Column dtype Inspection:
*Battalion Unique Values:* ignore
8.0 nan 1.0 6.0 5.0 4.0 12.0 2.0 16.0 20.0 ' ' '5' '6' '12' '4' '2' '1'
'19' '17' '3' '7' '15' '18' 'SBC' '14' '13' '11' '8' '16' 'MMU' '9' 9.0
3.0 7.0 15.0

 *GLOBALID* ignore
 Length: 132522, dtype: str
 NOTES: Not unique to one structure, listed as a unique value for each entry into the database = unusable as a unique structural identifier.


*APN (parcel)* Represents a land parcel(can contain multiple structures) 
Unique APN total: 78176
<ipython-input-6-51b9c4a4f55a>:6: DtypeWarning: Columns (0: Battalion, 1: Fire Name (Secondary), 2: APN (parcel)) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv(csv_path)

APN (parcel)
018060086000       258
                   254
050-150-111-000    168
4414021025         155
173-030-001        135
041-430-029-000    113
051-020-060        109
411210002          109
223-030-016        106
1250904341         104
086-011-27          99
055-290-052-000     97
066-430-008-000     96
11309013T           87
032100034000        85
034-011-063         83
11004009T           82
054-120-021-000     78
050-190-039-000     78
050-190-053-000     76
Name: count, dtype: int64 


*Site Address (parcel)* ignore
73890
<ipython-input-8-f19625d90f45>:6: DtypeWarning: Columns (0: Battalion, 1: Fire Name (Secondary), 2: APN (parcel)) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv(csv_path)
Site Address (parcel)
                                                              1850
 LAKESHORE CA 93634                                            590
No Address Available                                           513
                                                               488
580 LOMMEL RD CALISTOGA CA 94515                               258
ECHO LAKE CA 95721                                             203
NULL  NULL    UNKNOWN CA 00000                                 160
16001 PACIFIC COAST HWY, PACIFIC PALISADES, CA 90272           160
16321 PACIFIC COAST HWY SPC 1, PACIFIC PALISADES, CA 90272     155
1400  KILCREASE CIR   PARADISE CA 95969                        154
518 ANGELUS ST SANTA ROSA CA 95403                             135
 SHAVER LAKE CA 93664                                          130
2920 CLARK RD SPC 21A BUTTE VALLEY CA 95965                    113
7425 RANCHO LOS GUILICOS RD SANTA ROSA CA 95409                109
1134 VILLA CALIMESA LN SPC E12 CALIMESA CA 92320               109
354  SCHOOL ST CA 93238                                        106
4650 DULIN RD                                                  104
6674  PENTZ RD   PARADISE CA 95969                              98
5110  PENTZ RD   PARADISE CA 95969                              96
9289  SKYWAY     MAGALIA CA 95954                               96
Name: count, dtype: int64



# Finalized CSV File for CalFIRE's DINS Report from the 2018 Camp Fire in Butte County California
data\camp_fire_structures.csv
