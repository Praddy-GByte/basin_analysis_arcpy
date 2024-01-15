import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
dem_raster = "dem.tif"  # Digital Elevation Model (DEM) of the area
land_cover_raster = "land_cover.tif"  # Land cover raster data
stream_network = "streams.shp"  # Stream network shapefile

# Output data
erosion_output = "erosion_risk.tif"

# Step 1: Fill sinks in the DEM
filled_dem = Fill(dem_raster)

# Step 2: Calculate LS Factor for erosion
ls_factor = Ln((FlowAccumulation("FLOW_DIRECTION") * 30) / Tan(Slope(filled_dem)))
ls_factor.save("ls_factor.tif")

# Step 3: Erosion risk analysis
erosion_risk = Con((Raster(land_cover_raster) == "Urban") & (FlowAccumulation("FLOW_DIRECTION") > 1000), 1, 0)
erosion_risk.save(erosion_output)

# Print completion message
print("Erosion Analysis completed.")
