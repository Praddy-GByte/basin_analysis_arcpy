import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
dem_raster = "dem.tif"  # Digital Elevation Model (DEM) of the area
stream_network = "streams.shp"  # Stream network shapefile

# Output data
watershed_output = "watershed.shp"
flow_accumulation_output = "flow_accumulation.tif"
stream_order_output = "stream_order.shp"

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

# Step 7: Stream ordering
arcpy.gp.StreamOrder_sa(stream_network, stream_order_output, "STRAHLER")

# Step 8: Basin morphometry
arcpy.gp.BasinMorphometry_sa(watershed_output, dem_raster, "BASIN_MORPHOMETRY.dbf")

# Step 9: Drainage density
arcpy.gp.DrainageDensity_sa(stream_network, "DRAINAGE_DENSITY.dbf")

# Additional steps can include statistics, land cover analysis, etc.

# Print completion message
print("River basin analysis and morphometric analysis completed.")
