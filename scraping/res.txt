import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import csv

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Collect the github page
html = urlopen('https://github.com/trending', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)

art = soup.find_all('article',class_='Box-row')
des = soup.find_all('p',class_='col-9 text-gray my-1 pr-4')
strs = soup.find_all('div',class_='f6 text-gray mt-2')
file_name = "github_trending_today.csv"
f = csv.writer(open(file_name, 'w', newline='',encoding="UTF-8"))
f.writerow(['Developer', 'Repo Name', 'Number of Stars','Description','Link'])
for i in range(len(art)):
   name = art[i].h1.text
   name.rstrip()
   name.lstrip()
   lis = name.split('/')
   dname = str(lis[0].strip())
   rname = str(lis[1].strip())
   stars = str(strs[i].a.text.strip())
   descrip = str(des[i].text.strip())
   link = 'https://github.com/'+dname+'/'+rname
   print(dname)
   print(rname)
   print(stars)
   f.writerow([dname, rname, stars,descrip,link])
