import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
dem_raster = "dem.tif"  # Digital Elevation Model (DEM) of the area
land_cover_raster = "land_cover.tif"  # Land cover raster data
watershed_output = "watershed.shp"

# Output data
land_cover_output = "land_cover_in_watershed.tif"
land_cover_statistics_output = "land_cover_statistics.csv"

# Step 1: Fill sinks in the DEM
filled_dem = Fill(dem_raster)

# Step 2: Delineate watershed
arcpy.gp.Watershed_sa(flow_direction, stream_network, watershed_output)

# Step 3: Clip land cover raster to watershed boundary
arcpy.Clip_management(land_cover_raster, "", land_cover_output, watershed_output, "", "ClippingGeometry")

# Step 4: Calculate land cover statistics
land_cover_statistics = ZonalStatistics(watershed_output, "OBJECTID", land_cover_output, "MAJORITY", "DATA")
land_cover_statistics.save(land_cover_statistics_output)

# Print completion message
print("Land Cover Analysis completed.")
