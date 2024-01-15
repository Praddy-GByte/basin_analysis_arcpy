import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set your workspace
arcpy.env.workspace = r"C:\path\to\your\workspace"

# Input data
precipitation_raster = "precipitation.tif"  # Precipitation data raster
temperature_raster = "temperature.tif"  # Temperature data raster

# Output data
drought_risk_output = "drought_risk.tif"

# Step 1: Analyze historical drought events
historical_drought = Con((Raster(precipitation_raster) < 50) & (Raster(temperature_raster) > 30), 1, 0)

# Step 2: Assess vulnerability to future droughts
future_drought_risk = Con((Raster(precipitation_raster) < 40) & (Raster(temperature_raster) > 35), 1, 0)

# Combine historical and future drought risks
combined_drought_risk = historical_drought + future_drought_risk
combined_drought_risk.save(drought_risk_output)

# Print completion message
print("Drought Risk Assessment completed.")
