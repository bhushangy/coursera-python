import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
from urllib.request import Request, urlopen

req = Request('https://www.pornpics.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#url = 'https://pixabay.com/'
#html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(webpage,"html.parser")

art = soup.find_all('img',{"src":True}) #means only those img tags with src attribute
#print(art)
lis1 = list()

for i in art:  # see here art is a list of dictionary like tags...so ur iterating thru i dic at a time
    lis1.append((i.get('data-src')))  # or use i.get('src')..here each i is an image tag and within that image tag u get src
print(lis1)

file = open('trend.jpg','w',encoding="utf-8")

for j in lis1:
    if not j.startswith("https"):
    	continue
    urllib.request.urlretrieve(str(j), "trend.jpg")
    