# Import the modules required for this project
import numpy as np
import rasterio as rio
import matplotlib.pyplot as plt

# NDVI Function
def calculate_ndvi(red, nir):
    """Calculate NDVI from Red and NIR raster bands"""

    # Convert arrays to floating point numbers
    red = red.astype('float32')
    nir = nir.astype('float32')

    # ndvi calculation
    ndvi = (nir - red) / (nir + red)
    result = ndvi

    return ndvi

# Print georeferencing information function
def print_stats(dataset):
    """Print statistics about the dataset"""

    # Display the metadata and georeferencing information for the raster
    print(f"{dataset.name} opened in {dataset.mode} mode")
    print(f"Image has {dataset.count} bands")
    print(f"Raster size: {dataset.width} x {dataset.height}")
    print(f"Raster CRS: {dataset.crs}")
    print(f"Raster bounds: {dataset.bounds}")

# Load bands function
def load_bands(dataset):
    """Load bands from dataset"""

    # read red and near infrared bands
    red = dataset.read(3) # Landsat 5 TM Band 3 = red
    nir = dataset.read(4) # Landsat 5 TM Band 4 = near infrared

    result = red, nir
    return result

# Print NDVI min, max and mean function
def print_ndvi_stats(ndvi):
    """Print NumPy NDVI Calculations"""

    # NumPy nanmin, nanmax and nanmean function used to ignore NaN values for NDVI calculations
    print(f"NDVI minimum value: {np.nanmin(ndvi)}")  # show the NDVI minimum value
    print(f"NDVI maximum value: {np.nanmax(ndvi)}")  # show the NDVI maximum value
    print(f"NDVI mean: {np.nanmean(ndvi)}")  # show the NDVI mean value

# Results visualization function
def plot_ndvi(ndvi):
    """Display the results of the NDVI calculations"""

    # Visualize the results
    plt.figure(figsize=(10, 8))
    plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
    plt.colorbar(label='NDVI')
    plt.title("NDVI calculated from Landsat 5 TM Imagery")
    plt.show()

# File path to the Landsat 5 TM raster used for this project
raster_path = r"C:\egm722_projects\egm722\Week4\data_files\NI_Mosaic.tif"

# Ignore divide by zero errors caused by invalid raster pixels
np.seterr(divide='ignore', invalid='ignore')

# Open the raster using with statement
with rio.open(raster_path) as dataset:

    # Load bands function call
    red, nir = load_bands(dataset)

    # Print band array shape
    print(f"Red band shape: {red.shape}")
    print(f"NIR band shape: {nir.shape}")

    # Print statistics function call
    print_stats(dataset)

    # NDVI function call
    ndvi = calculate_ndvi(red, nir)

    # NDVI statistics function call
    print_ndvi_stats(ndvi)

    # Copy metadata from the original raster
    ndvi_meta = dataset.meta.copy()

    # Update metadata for output NDVI raster
    ndvi_meta.update({"count": 1, "dtype": "float32"})

    # Save output as GeoTIFF file
    with rio.open("outputs/ndvi_output.tif", "w", **ndvi_meta) as dst: