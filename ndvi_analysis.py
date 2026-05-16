# Import the modules required for this project
import numpy as np
import rasterio as rio
import matplotlib.pyplot as plt

# File path to the Landsat 5 TM raster used for this project
raster_path = r"C:\egm722_projects\egm722\Week4\data_files\NI_Mosaic.tif" # r mode used to ensure file path behaves

# Open the raster using with statement
with rio.open(raster_path) as dataset:
    red = dataset.read(3) # Landsat 5 TM Band 3 = red
    nir = dataset.read(4) # Landsat 5 TM Band 4 = near infrared

    print(f"{dataset.name} opened in {dataset.mode} mode")
    print(f"Image has {dataset.count} bands")
    print(f"Raster size: {dataset.width} x {dataset.height}")
    print(f"Red band shape: {red.shape}")
    print(f"NIR band shape: {nir.shape}")