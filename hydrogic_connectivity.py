import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
dem_raster = "dem.tif"  # Digital Elevation Model (DEM) of the area
stream_network = "streams.shp"  # Stream network shapefile
sink_output = "sinks.tif"

# Output data
connectivity_output = "hydrological_connectivity.tif"

# Step 1: Fill sinks in the DEM
filled_dem = Fill(dem_raster)

# Step 2: Identify sinks
sinks = Sink(filled_dem)
sinks.save(sink_output)

# Step 3: Hydrological connectivity
connectivity = FlowLength(sinks, "DOWNSTREAM", "")
connectivity.save(connectivity_output)

# Print completion message
print("Hydrological Connectivity Analysis completed.")
