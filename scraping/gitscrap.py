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

art = soup.find_all('article',class_='Box-row')               or   # art = soup.find_all('span',clas='text-normal')
des = soup.find_all('p',class_='col-9 text-gray my-1 pr-4')   or   # art = soup.find_all('h1',class_='h3 lh-condensed'))  
strs = soup.find_all('div',class_='f6 text-gray mt-2')
file = open('trend.txt','w',encoding="utf-8")
for i in range(len(art)):
   name = art[i].h1.text
   name.rstrip()
   name.lstrip()
   lis = name.split('/')
   dname = str(lis[0].strip())
   rname = str(lis[1].strip())
   stars = str(strs[i].a.text.strip())
   descrip = str(des[i].text.strip())
   print(dname)
   print(rname)
   print(stars)
   file.write(str(i+1) +') '+'Name: '+dname)
   file.write("\n")
   file.write('Repo: '+rname)
   file.write("\n")
   file.write('Stars: '+stars)
   file.write("\n")
   file.write('Link: '+'https://github.com/'+dname+'/'+rname)
   file.write("\n")
   file.write('Desc: '+descrip)
   file.write("\n")
   file.write("\n")
   print('\n')
