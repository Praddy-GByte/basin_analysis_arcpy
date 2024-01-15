import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
land_cover_raster = "land_cover.tif"  # Land cover raster data
stream_network = "streams.shp"  # Stream network shapefile

# Output data
habitat_output = "habitat_assessment.tif"

# Step 1: Identify riparian areas
riparian_areas = Con((Raster(land_cover_raster) == "Forest") & (StreamOrder(stream_network) == 1), 1, 0)
riparian_areas.save("riparian_areas.tif")

# Step 2: Combine riparian areas with other habitat factors
habitat_assessment = Con((riparian_areas == 1) | ((Raster(land_cover_raster) == "Wetland") & (StreamOrder(stream_network) >= 2)), 1, 0)
habitat_assessment.save(habitat_output)

# Print completion message
print("Habitat Assessment completed.")
