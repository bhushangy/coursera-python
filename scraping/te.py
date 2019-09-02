import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Collect the github page
html = urlopen('https://github.com/trending', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)



l1 = list()
l2 = list()
dname = list()
rname = list()
art = soup.find_all('h1',class_='h3 lh-condensed')
for i in range(len(art)):
	l1.append(str(art[i].text).strip())
	l2 = l1[0].split('/')	
	dname = l2[0]
	rname = l2[1]

print(dname)
print(rname)