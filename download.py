import urllib.request
def downld(ad):
    url=ad
    root="D://"
    path=root+url.split('/')[-1]
    urllib.request.urlretrieve(url,path)
