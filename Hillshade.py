import os
import glob
from osgeo import gdal 
import subprocess

path = 'R:\DEM\R4_USGS_NED_10m.tif'


raster = gdal.Open(path,gdal.GA_ReadOnly)

gdaldem hillshade raster test.tif -s 111120 -z 5 -az 315 -alt 60 -compute_edges  