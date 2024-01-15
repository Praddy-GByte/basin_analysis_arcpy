import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
land_cover_raster = "land_cover.tif"  # Land cover raster data
stream_network = "streams.shp"  # Stream network shapefile
water_quality_raster = "water_quality.tif"  # Water quality data raster

# Output data
water_quality_output = "water_quality_assessment.tif"

# Step 1: Extract land cover near streams
land_cover_near_streams = ExtractByMask(land_cover_raster, stream_network)
land_cover_near_streams.save("land_cover_near_streams.tif")

# Step 2: Assess water quality based on land cover
water_quality_assessment = Con((land_cover_near_streams == "Urban") & (water_quality_raster > 5), 1, 0)
water_quality_assessment.save(water_quality_output)

# Print completion message
print("Water Quality Analysis completed.")
