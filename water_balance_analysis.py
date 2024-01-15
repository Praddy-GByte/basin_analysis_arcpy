import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
precipitation_raster = "precipitation.tif"  # Precipitation data raster
evaporation_raster = "evaporation.tif"  # Evaporation data raster
runoff_raster = "runoff.tif"  # Runoff data raster

# Output data
water_balance_output = "water_balance.tif"

# Step 1: Evaluate water balance components
water_balance = Raster(precipitation_raster) - Raster(evaporation_raster) - Raster(runoff_raster)
water_balance.save(water_balance_output)

# Print completion message
print("Water Balance Analysis completed.")
