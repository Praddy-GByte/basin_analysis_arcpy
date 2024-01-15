import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
land_cover_raster = "land_cover.tif"  # Land cover raster data
stream_network = "streams.shp"  # Stream network shapefile

# Output data
wildlife_connectivity_output = "wildlife_connectivity.tif"

# Step 1: Identify suitable habitat for wildlife
suitable_habitat = Con(Raster(land_cover_raster) == "Forest", 1, 0)

# Step 2: Analyze connectivity for wildlife movement
connectivity_analysis = StreamLink(suitable_habitat, stream_network)
wildlife_connectivity = StreamToFeature(connectivity_analysis, stream_network, "WILDLIFE_CONNECTIVITY", "NO_SIMPLIFY")
wildlife_connectivity.save(wildlife_connectivity_output)

# Print completion message
print("Connectivity Analysis for Wildlife Movement completed.")
