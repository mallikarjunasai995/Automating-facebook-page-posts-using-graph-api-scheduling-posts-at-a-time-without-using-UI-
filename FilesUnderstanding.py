# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 04:44:59 2020

@author: malli
"""

import os
from os import listdir
#from PIL import Image as PImage


def loadImages(path):
    for count,filename in enumerate(listdir(path)):
        dst = "imgnns"+str(count)+".jpg"
        src = path +'\\'+filename
        dst = path +'\\'+dst
        os.rename(src, dst)
        
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = path +'\\'+image
        
        loadedImages.append(img)
        print(img)

    return loadedImages

path = r'C:\Users\malli\OneDrive\Desktop\Embedded\python\Python_Autoamtion\Vocabulary-Fbpage\templatesdesigns'

imgs = loadImages(path)
print(type(imgs))

# for img in imgs:
#     img.show()
    
    
    

# for count, filename in enumerate(os.listdir("xyz")): 
#         dst ="Hostel" + str(count) + ".jpg"
#         src ='xyz'+ filename 
#         dst ='xyz'+ dst 
          
#         # rename() function will 
#         # rename all the files 
           
    
    
    
#from pathlib import Path
#script_dir = os.path.dirname(__file__)
#print(script_dir)
#rel_path ='Vocabulary-Fbpage\templatesdesigns' 
#abs_file_path = os.path.join(script_dir, rel_path)
#print(abs_file_path)
#howtoopen an image
