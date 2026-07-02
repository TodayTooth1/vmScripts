#This script is used to convert an ESRI ArcGIS Pro DEM raster .dat file into a .raw file used in Unity. 

import numpy as np

input_file = r"E:\prototype\datfiles\paradiseDEM.dat"
output_file = r"E:\prototype\datfiles\paradiseDEM.raw"

#DEM Stats from ArcGIS
elev_min = 183 #meters
elev_max = 727 #meters
elev_range = elev_max - elev_min

#DEM dimensions
rows = 1024
cols = 1024

# Load the .dat file (Normalized 0-255)
data = np.fromfile(input_file, dtype=np.uint8)

#Convert back to real elevation (meters)
real_elevation = elev_min + (data / 255.0) * elev_range

#Normalize to Unity RAW range (0-65535)
raw_16bit = ((real_elevation - elev_min) / elev_range * 65535).astype(np.uint16)

#Reshape to 2D
raw_16bit_2d = raw_16bit.reshape((rows,cols))

# Flip vertically (top/bottom) and horizontally (left/right)
raw_16bit = np.flipud(raw_16bit_2d) #vertical
raw_16bit = np.fliplr(raw_16bit_2d)  #horizontal

#flatten back to 1D for .raw export
raw_16bit_2d.flatten().tofile(output_file)

print(f"Saved {output_file} successfully!")
print(f"Elevation range preserved: {elev_min} to {elev_max} meters")
