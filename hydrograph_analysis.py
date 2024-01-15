import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
stream_network = "streams.shp"  # Stream network shapefile
rainfall_raster = "rainfall.tif"  # Rainfall data raster
watershed_output = "watershed.shp"

# Output data
hydrograph_output = "hydrograph.csv"

# Step 1: Delineate watershed
arcpy.gp.Watershed_sa(stream_network, rainfall_raster, watershed_output)

# Step 2: Calculate hydrograph
hydrograph = ZonalStatisticsAsTable(watershed_output, "ID", rainfall_raster, hydrograph_output, "DATA", "SUM")
hydrograph.save(hydrograph_output)

# Print completion message
print("Hydrograph Analysis completed.")
