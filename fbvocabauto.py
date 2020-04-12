import requests
import time
import os
from os import listdir
from PIL import Image as PImage


def loadImages(path):
    for count,filename in enumerate(listdir(path)):
        dst = "img"+str(count)+".jpg"
        src = path +'\\'+filename
        dst = path +'\\'+dst
        os.rename(src, dst)
        
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = path +'\\'+image
        
        loadedImages.append(img)

    return loadedImages

path = r'C:\Users\malli\OneDrive\Desktop\Embedded\python\Python_Autoamtion\Vocabulary-Fbpage\templatesdesigns'

imgs = loadImages(path)
print(type(imgs))

#epochtimeunix remember
def calepoch():
    
    t = int(time.time() + 97400)
    return t


img_path = r'C:\Users\malli\OneDrive\Desktop\Embedded\python\Python_Autoamtion\Vocabulary-Fbpage\templatesdesigns\img11.jpg'


params = (
    ('published', 'false'),
    ('scheduled_publish_time', '{}'.format(calepoch())),
    ('access_token', 'EAAOVvtAzc6IBAOa6BJy67udgZC7GTZAPUxbaTgetGaphn2WGncHPEFZBiNMgzK2SZC7KSkhUW77KlBwm0SZBXnjZBBTwLZClvYWVFc6HjGwBTU4y6s5HeZBbhOicRyYElS3YQp84auYCF1xZCbBKeRrXAZACiGaeK3qTMx6tD1ZANLdlzqf1OliHL9ZCPArHTQ1Mc1YV3E9rBuEHigZDZD'),
)

files = {'file': open(img_path,'rb')}

response = requests.post('https://graph.facebook.com/v6.0/1194256010637631/photos', params=params, files=files)
#print(params)
print(response)
