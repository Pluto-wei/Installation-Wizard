import urllib.request
import os
def downld(ad):
    url=ad
    root="C://"
    path=root+url.split('/')[-1]
    urllib.request.urlretrieve(url,path)
#def install(name):
    #os.startfile(name)    #失败
