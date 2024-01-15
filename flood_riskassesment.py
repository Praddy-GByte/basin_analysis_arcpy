import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
dem_raster = "dem.tif"  # Digital Elevation Model (DEM) of the area
land_cover_raster = "land_cover.tif"  # Land cover raster data
stream_network = "streams.shp"  # Stream network shapefile
watershed_output = "watershed.shp"

# Output data
flood_prone_areas_output = "flood_prone_areas.tif"
flood_risk_zones_output = "flood_risk_zones.shp"

# Step 1: Fill sinks in the DEM
filled_dem = Fill(dem_raster)

# Step 2: Flow direction
flow_direction = FlowDirection(filled_dem)

# Step 3: Flow accumulation
flow_accumulation = FlowAccumulation(flow_direction)

# Step 4: Stream threshold
stream_threshold = Con(flow_accumulation > 100, 1)

# Step 5: Stream to feature
arcpy.RasterToPolyline_conversion(stream_threshold, stream_network, "ZERO", "0", "SIMPLIFY", "VALUE")

# Step 6: Delineate watershed
arcpy.gp.Watershed_sa(flow_direction, stream_network, watershed_output)

# Step 7: Extract flood-prone areas based on elevation
elevation_threshold = 10  # Adjust the threshold based on your study
flood_prone_areas = Con(filled_dem < elevation_threshold, 1, 0)
flood_prone_areas.save(flood_prone_areas_output)

# Step 8: Extract flood risk zones based on land cover
land_cover_threshold = "Urban"  # Adjust the land cover class based on your study
flood_risk_zones = Con(Raster(land_cover_raster) == land_cover_threshold, 1, 0)
flood_risk_zones.save(flood_risk_zones_output)

# Print completion message
print("Flood Risk Assessment completed.")
