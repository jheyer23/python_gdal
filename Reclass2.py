import os
import glob
from osgeo import gdal 
import subprocess
import numpy as np
#import future_fstrings

path = "B:\Reclass_NoData"
#path = os.getcwd()
os.chdir(path)
#pattern = '*.tif'
#print(pattern) 

# Create list of rasters 
in_directory= path
images = glob.glob(os.path.join(in_directory, '*.tif'))
print(images) 

#The enumerate() method adds counter to an iterable and returns it. The returned object is a enumerate object. 
# GetDriverByName -Determines if the tif format supports Create or CreateCopy (Creating tif raster - GTiff)  
for i, data_path in enumerate(images):
    raster = gdal.Open(data_path,gdal.GA_ReadOnly)
    file_name = os.path.splitext(os.path.split(data_path)[1])[0]
    output_path = "B:/reclass_images/{file_name}_reclassified_test.tif".format(**locals())
    myarray = raster.GetRasterBand(1).ReadAsArray()
    myarray[np.where(myarray != -32768)] = 1
    myarray[np.where(myarray > -32768)] = 2
    driver = gdal.GetDriverByName('GTiff')
    file_out = driver.Create(output_path, raster.RasterXSize , raster.RasterYSize , 1)
    file_out.GetRasterBand(1).WriteArray(myarray)
    proj = raster.GetProjection()
    georef = raster.GetGeoTransform()
    meta = raster.GetMetadata()
    file_out.SetProjection(proj)
    print('SetProjection')
    file_out.SetGeoTransform(georef)
    print('GeoTransform extent')
    file_out.SetMetadata(meta)
    print('SetMetadata')
    file_out.FlushCache()
     

