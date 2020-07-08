# Subprocesses module - Way to communicate between scripts and between languages. For example, I have used this to communicate between python and GDAL 
# Replaces modules like os system, os piping and some commands 
# Allows you to communicate between script to shell and get output to shell
# Shell is a user interface (e.g. cmd) for access to an OS (operating systems) services. Soley text-based. Can type commands and perform functions to run programs, open and browse directory, and view processes that are currently running. Shell is layer above OS
# Call external commands - can pipe output from one command to another 
# Run external commands 

import subprocess 

# List files and folders in current directory 
# shell = true; dir command built into shell - can pass in entire command as string 
# Only use shell command if using it on my own machine. Can be a security issue 
# Capture into variable - stdout 
process1 = subprocess.run('dir', shell = True)
print(process1)

# See arguments passed into subprocess.run command ('dir')
print(process1.args)

# Pass return code to see if we had any errors. Return code of 0 = zero errors - ran successfully 
print(process1.returncode)

# Print out stdout (standard out) 
# Prints "None" because stdout not captured 
print(process1.stdout)

# Capture stdout 
# This captures it as bites 
# Pass in additional argument to redirect stdout to a string (stdout=subprocess.Pipe) 
process2 = subprocess.run('dir', shell = True, stdout=subprocess.PIPE)

# Capture stdout as a string 
print(process2.stdout.decode()) 

# Redirect stdout as a file 
# Redirect stdout to file 
import os 
path = "D:/Python_Learning"
os.chdir(path) 

# 'w' writes file to directory 
with open('output.txt', 'w') as file: 
    p1 = subprocess.run('dir', shell= True, stdout=file) 
    
# Dealing with errors 
# Make up some directory that doesn't exist 
path = "D:/Python_Learn"
os.chdir(path) 
process3 = subprocess.run(['path'], shell = True, stdout=subprocess.PIPE)

# print out error 
print(process3.stderr)

# Can open a program by directing to the program .exe 
chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
subprocess.check_call([chrome, '--kiosk'])

# Popen example 

#path = "D:/TCC_Zones/Mosaic_test"
path = os.getcwd()
os.chdir(path)
pattern = '*.tif'
output_name = os.path.join(path,'Tile40_DR1_Julian_Day_Stats.tif')


# Create list of rasters 
images = [os.path.join(path,i) for i in glob.glob(pattern)]

#Ensure existing output isnt in list of images
images = [i for i in images if i != output_name]
print(images, "list of images") 


def check_dir(d):
    if os.path.exists(d) == False:os.makedirs(d)
def base(p):
    return os.path.basename(os.path.splitext(p)[0])
def merge_rasters(image_list,output_name):
    #Set up vrt dir
    vrt_dir = os.path.join(os.path.dirname(output_name), 'VRTs/')
    check_dir(vrt_dir)

    #Make vrt image
    vrt_image = vrt_dir + base(output_name) + '.vrt'
    if os.path.exists(vrt_image) == False:
        c = 'gdalbuildvrt' +vrt_image 
        for image in image_list:
            c += ' '+image
        call = subprocess.Popen(c)
        call.wait()
    
    # Popen(Arguments (gdal program arguments to merge, compress large raster), bufsize (ignored here), executable (ignored here), stdin (virtual images), stout (output_name object) 
    # Popen redirects the stdin (input files - virtual images here) to a stdout (output_name - directory file name object made above)
    if os.path.exists(output_name) == False:
        c = 'gdal_translate -co "COMPRESS=LZW" -co "BIGTIFF=YES" '+vrt_image + ' '+ output_name  
        print(c)
        call = subprocess.Popen(c)
        call.wait()
        c = 'gdaladdo '+ output_name
        print(c)
        call = subprocess.Popen(c)
        call.wait()
        # set_no_data(output, -32768, update_stats = True)
    #     set_projection(output,collectionDict[studyAreaName]['gdal_crs']) 
        


# ITERATE THROUGH LIST OF IMAGES AND EXECUTE FUNCTIONS ON EACH IMAGE
   
merge_rasters(images, output_name)
