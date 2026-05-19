# NDVI Analysis using Landsat 5 TM Imagery

## Description
This repository contains a Python workflow for calculating Normalized Difference Vegetation Index (NDVI) from Landsat 5 TM imagery. The project uses rasterio, NumPy and matplotlib to read raster bands, calculate NDVI, output the result and export in the GeoTIFF file format.

## Outputs
The script produces:

	- an NDVI visualisation using matplotlib
	- a GeoTIFF raster file called 'ndvi_output.tif'
The GeoTIFF raster is saved in the 'outputs' folder of the project directory.

## Dataset
A raster dataset titled 'NI_Mosaic.tif', provided in the EGM722 Week 4 practical materials is used in this project. The dataset should be placed inside the 'data' folder within the project directory.

The workflow is designed to function with Landsat 5 TM imagery where:
	- Band 3 corresponds to the red band
	- Band 4 corresponds to the NIR band

For this script to work with other multispectral raster datasets, the band numbers used in the 'load_bands()' function must be modified before use. This function loads the correct bands, NIR and red, for the script to calculate NDVI, so any external datasets must include the correct band number.

## Installation/Setup
Pre-requisite software requirements:

	- Python 3.x
	- Anaconda
	- Git
	- PyCharm
Required python modules (dependencies):

	- rasterio
	- NumPy
	- matplotlib
Installation instructions:

	1. Navigate to the repository page: 'https://github.com/Blair-N7/egm722-ndvi-project'.
	2. Click the green 'Code' button.
	3. Select 'Download Zip'.
	4. Extract the downloaded ZIP file to a suitable folder.
	5. Open Anaconda, click the 'Environments' tab, click 'Import'.
	6. In the 'Import Environment' window that opens, tick Local drive and browse to the directory of the extracted ZIP            file of the repository, click 'environment.yml', then click 'Import'.
	7. Navigate to the folder of the extracted ZIP file, right click and open 'ndvi_analysis' with PyCharm.
	8. If prompted, select 'Conda' as the Python interpreter created from 'environment.yml', this can also be done via 	           PyCharm settings
	9. With ndvi_analysis open in the prloject panel, click the green run button to execute the script.

## Repository Link
URL: https://github.com/Blair-N7/egm722-ndvi-project