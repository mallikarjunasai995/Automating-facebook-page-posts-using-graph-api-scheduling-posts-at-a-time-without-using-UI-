import requests
import time
import os
from os import listdir
#from PIL import Image as PImage

def loadImages(path):
    for count,filename in enumerate(listdir(path)):
        dst = "imd"+str(count)+".jpg"
        src = path +'\\'+filename
        dst = path +'\\'+dst
        os.rename(src, dst)
        
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = path +'\\'+image
        
        loadedImages.append(img)

    return loadedImages

path = r'C:\\Desktop\Embedded\python\Python_Autoamtion\Vocabulary-Fbpage\templatesdesigns'

imgs = loadImages(path)
print(type(imgs))


#epochtimeunix remember
def calepoch(ct):
    
    d = 86400
    ct = ct + 1
    t = int(time.time() + d*ct )
    print(t)
    return t


#img_path = r'C:\Users\malli\OneDrive\Desktop\Embedded\python\Python_Autoamtion\Vocabulary-Fbpage\templatesdesigns\img11.jpg'




for ct,img in enumerate(imgs):
    
    params = (
    ('published', 'false'),
    ('scheduled_publish_time', '{}'.format(calepoch(ct))),
    ('access_token', 'yourpageaccesstoken'),
     )
    

    files = {'file': open(img,'rb')}

    response = requests.post('https://graph.facebook.com/v6.0/1194256010637631/photos', params=params, files=files)
        #print(params)
    print(response)




















