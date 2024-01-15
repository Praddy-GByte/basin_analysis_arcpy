import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
dem_raster = "dem.tif"  # Digital Elevation Model (DEM) of the area
slope_raster = Slope(dem_raster)

# Output data
landslide_susceptibility_output = "landslide_susceptibility.tif"

# Step 1: Evaluate terrain stability and slope characteristics
slope_threshold = 20  # Adjust the threshold based on your study
slope_mask = Con(slope_raster > slope_threshold, 1, 0)

# Step 2: Generate landslide susceptibility map
landslide_susceptibility = slope_mask * FlowAccumulation(dem_raster)
landslide_susceptibility.save(landslide_susceptibility_output)

# Print completion message
print("Landslide Susceptibility Mapping completed.")
