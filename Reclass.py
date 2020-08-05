import os
import glob
from osgeo import gdal 
import subprocess
import numpy as np

path = "B:/GDAL_processing"
os.chdir(path)
pattern = '*.tif'
inRaster = glob.glob(pattern)


#https://gis.stackexchange.com/questions/163007/raster-reclassify-using-python-gdal-and-numpy/193100#193100
infile= r"B:\Reclass_NoData\Tile_25_Landtrendr_Fitted_2011_182_244.TIF"
path_outDs = "B:/Reclass_NoData/reclassTest.tif"

raster = gdal.Open(infile,gdal.GA_ReadOnly)
band = raster.GetRasterBand(1)
lista = band.ReadAsArray()


lista[np.where(lista != -32768)] = 1
lista[np.where(lista >= -32768)] = 2


#https://stackoverflow.com/questions/51719096/create-geotiff-gdal-from-np-array
# create new file
# Determine if the tif format supports Create or CreateCopy (Creating tif raster - GTiff) - Didn't work with Gimg - maybe need to write out differently  
driver = gdal.GetDriverByName('GTiff')
file2 = driver.Create(path_outDs, raster.RasterXSize , raster.RasterYSize , 1, gdal.GPI_RGB)
print 'Creating reclass raster'
file2.GetRasterBand(1).WriteArray(lista)


# spatial ref system
proj = raster.GetProjection()
georef = raster.GetGeoTransform()
meta = raster.GetMetadata()

file2.SetProjection(proj)
print 'SetProjection',raster,'to',file2
file2.SetGeoTransform(georef)
print 'GeoTransform extent',raster, 'to', file2 
file2.SetMetadata(meta)
print 'SetMetadata', raster, 'to', file2 

file2.FlushCache()
del file2

# https://gis.stackexchange.com/questions/327280/reclassify-multiple-raster-files-with-gdal
# Loop thru multiple rasters 