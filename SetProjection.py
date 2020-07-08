import os
import glob
from osgeo import gdal 
import subprocess

path = os.getcwd()
os.chdir(path)
pattern = '*.tif'
print(pattern) 

# Create list of rasters 
images = glob.glob(pattern)


def set_projection(image,crs):
    rast = gdal.Open(image, gdal.GA_Update)
    rast.SetProjection(crs)
    rast = None

# EPSG 7019: Geodetic Reference System GRS 1980 
# EPSG 6269: North American Datum 1963 (Geodetic CRS: NAD83; Ellipsoid: GRS 1980; Prime meridian: Greenwich)
# EPSG 8091: The international reference meridian (i.e. Greenwich)
# EPSG 9108: GCS_North_American_1983
# EPSG 4269: NAD83 (Ellipsoid: GRS 1980; Prime meridian: Greenwich)

# Projection: Albers_Conic_Equal_Area 
   # standard_parallel_1: 29.5 latitude N
   # standard_parallel_2: 45.5 latitude N
   # latitude_of_center: 23 N 
   # Longitude of center: -96

gdal_crs = 'PROJCS["NAD_1983_Albers",GEOGCS["NAD83",DATUM["North_American_Datum_1983",SPHEROID["GRS1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6269"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9108"]],AUTHORITY["EPSG","4269"]],PROJECTION["Albers_Conic_Equal_Area"],PARAMETER["standard_parallel_1",29.5],PARAMETER["standard_parallel_2",45.5],PARAMETER["latitude_of_center",23],PARAMETER["longitude_of_center",-96],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["meters",1]]'

for image in images[0:]:
    set_projection(image,gdal_crs)

