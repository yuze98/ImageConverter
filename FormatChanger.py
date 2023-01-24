#https://github.com/creimers/heic-to-jpg/issues/4
#https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows
#follow the guide here 
#pip install wand
#download imageMagick

#@author: youssef hatem

import re
import os
from wand.image import Image as WImage
import traceback

#add current directory here
cur_dir = "D:/prop/i7_photos/new_year" #os.getcwd()
dir_file_names = os.listdir(cur_dir)
print('length of data:', len(dir_file_names))

# funcntion to covert heic to jpg and removes heic file
def HEICToJPG(file_name):
    fpath = cur_dir + '/'+file_name
    try:
        print('trying')
        with WImage(filename=fpath) as img:
            im = img.convert('jpeg')
            im.save(filename=fpath.replace('.HEIC','.JPG'))
            print('clear: ', fpath)
            os.remove(fpath)
        
    except:
        print(traceback.format_exc())

# funnction to delete useless AAE files 
def deleteFiles(fileName):
    fpath = cur_dir + '/'+fileName
    os.remove(fpath)
    print('removed AAE files!')

for file in dir_file_names:
    if re.search(".HEIC", file):
        HEICToJPG(file)
    elif re.search(".AAE", file):
        deleteFiles(file)