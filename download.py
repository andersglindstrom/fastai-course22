
from duckduckgo_search import DDGS
from fastcore.all import L

def search_images(keywords, max_images=200):
    return L(DDGS().images(keywords, max_results=max_images)).itemgot('image')

urls = search_images('bird photos', max_images=1)
print(urls[0])

from fastdownload import download_url
dest = 'bird.jpg'
download_url(urls[0], dest, show_progress=False)

##from fastai.vision.all import *
##im = Image.open(dest)
##im.to_thumb(256,256)
