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














#import facebook
# import requests
# params = (
#     ('url', 'https://www.satsignal.eu/wxsat/msg-1-fc-40.jpg'),
#     ('published', 'true'),
#     ('access_token', 'EAAOVvtAzc6IBAKo2nk9eYw9NqkQZCNxXfbnPPWiHZCxawXIA8Pzb4wLEsBSZAwhssWhm34XBQW4NIvx5wCZBzaJOzBHlzZBumVOzmdc8ZACty6rYbeOcYyRcmbXR9ZBtONDUTXPIGsM6eofA0oUVRHUBm5oHKLksgJy6ZBrZBuqGZBeZAPygaOZBaVKclKttI1bgRx1nd2i5EIZCBIAZDZD'),
# )

# response = requests.post('https://graph.facebook.com/v6.0/1194256010637631/photos', params=params)
# print(response)


#token = 'EAAOVvtAzc6IBAKXRmVWNcZATIZAFc1smUb4YCGm0wtTCLOt51m5sgmNZBpIerBtiehObBYCVlvzXYZA1kg1gbxpBQoalAo9q0ysfAUGwq84XWM79NWxY2GN98resDsOU9wDdl5xqc4C9vd8vum3UTVdWpbPAk1ZAk7OwZCLKebXMixAfiZAV6pI9Y66WeYlVAzOj26j8aFVkgZDZD'
#fb = facebook.GraphAPI(access_token=token)
# fb.put_object(parent_object='me', connection_name='feed', message='#staysafe #stayhome')
# #app-id : 1194256010637631
# #accesstoken : EAAOVvtAzc6IBAKXRmVWNcZATIZAFc1smUb4YCGm0wtTCLOt51m5sgmNZBpIerBtiehObBYCVlvzXYZA1kg1gbxpBQoalAo9q0ysfAUGwq84XWM79NWxY2GN98resDsOU9wDdl5xqc4C9vd8vum3UTVdWpbPAk1ZAk7OwZCLKebXMixAfiZAV6pI9Y66WeYlVAzOj26j8aFVkgZDZD


# # params = (
# #     ('published', 'false\n  '),
# #     ('message', 'A scheduled post\n  '),
# #     ('scheduled_publish_time', '{unix-time-stamp-of-a-future-date}'),
# # )
# params = (
#     ('message', 'Hello Everyone!\n  '),
#     ('access_token', '{EAAOVvtAzc6IBAKXRmVWNcZATIZAFc1smUb4YCGm0wtTCLOt51m5sgmNZBpIerBtiehObBYCVlvzXYZA1kg1gbxpBQoalAo9q0ysfAUGwq84XWM79NWxY2GN98resDsOU9wDdl5xqc4C9vd8vum3UTVdWpbPAk1ZAk7OwZCLKebXMixAfiZAV6pI9Y66WeYlVAzOj26j8aFVkgZDZD}'),
# )

# #response = requests.post('https://graph.facebook.com/%7Bpage-id%7D/feed%0A%20%20', params=params)

# response = requests.post('https://graph.facebook.com/%7B1194256010637631%7D/feed%0A%20%20', params=params)
# print(response)




















# # create a new Chrome sessions
# from selenium import webdriver
# import time 

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# # Navigate to the application home page

# option = Options()

# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")

# # Pass the argument 1 to allow and 2 to block
# option.add_experimental_option("prefs", { 
#     "profile.default_content_setting_values.notifications": 2 
# })

# driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)
# #driver = webdriver.Chrome(executable_path='path-of- driver\chromedriver.exe')
# driver.get('https://www.facebook.com')
# username = 'mallikarjunasai995@gmail.com'
# driver.get("https://www.facebook.com/")
# driver.find_element_by_id('email').send_keys(username)
# password = ''
# driver.find_element_by_id('pass').send_keys(password)
# driver.find_element_by_id('loginbutton').click()
# time.sleep(5)
# driver.find_element_by_id('u_fetchstream_1_5').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="rc.u_0_2z"]/div[1]/span/span/a').click()
# #driver.find_elements_by_class_name('_1mwp navigationFocus _395 _1mwq _4c_p _5bu_ _3t-3 _34nd _21mu _5yk1').click()
# #driver.find_element_by_link_text('Create post').click()

