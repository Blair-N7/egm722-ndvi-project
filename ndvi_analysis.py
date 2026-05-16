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

 # Display the metadata and georeferencing information for the raster
    print(f"{dataset.name} opened in {dataset.mode} mode")
    print(f"Image has {dataset.count} bands")
    print(f"Raster size: {dataset.width} x {dataset.height}")
    print(f"Raster CRS: {dataset.crs}")
    print(f"Raster bounds: {dataset.bounds}")
    print(f"Red band shape: {red.shape}")
    print(f"NIR band shape: {nir.shape}")

# Ignore divide by zero errors caused by invalid raster pixels
np.seterr(divide='ignore', invalid='ignore')

# Convert arrays to floating point numbers
red = red.astype('float32')
nir = nir.astype('float32')

# ndvi calculation defined according to the formula
ndvi = (nir - red) / (nir + red)

# NumPy nanmin, nanmax and nanmean function used to ignore NaN values
print(f"NDVI minimum value: {np.nanmin(ndvi)}") # show the NDVI minimum value
print(f"NDVI maximum value: {np.nanmax(ndvi)}") # show the NDVI maximum value
print(f"NDVI mean: {np.nanmean(ndvi)}") # show the NDVI mean value

plt.figure(figsize=(10, 8))
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(label='NDVI')
plt.title("NDVI calculated from Landsat 5 TM Imagery")
plt.show()


