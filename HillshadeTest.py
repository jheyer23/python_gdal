import os
from osgeo import gdal 
import subprocess

#subprocess.call(["gdaldem", "hillshade", r"R:\DEM\R4_USGS_NED_10m.tif", \
     #r"R:\DEM\test4.tif", "-z", "1.0", "-s", "111120.0", \
     #"-alt", "45.0", "-multidirectional"])

# "-az", "120.0", "240.0", "360.0"

#os.system("gdaldem hillshade -z 1 -s 111120 -alt 45 -alg ZevenbergenThorne -multidirectional R:/DEM/R4_USGS_NED_10m.tif R:/DEM/test6.tif")

os.system("gdaldem hillshade R:/DEM/R4_USGS_NED_10m.tif R:/DEM/test7.tif -co BIGTIFF=YES -co TILED=YES -co COMPRESS=DEFLATE -of GTiff -z 1.0 -s 0.5 -multidirectional")