import requests
import r
from bs4 import BeautifulSoup

# Collect the github page
page = requests.get('https://github.com/trending')
print(page)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

art = soup.find_all('article',class_='Box-row')
str = soup.find_all('div',class_='f6 text-gray mt-2')

for i in range(len(art)):
   name = art[i].h1.text
   name.rstrip()
   name.lstrip()
   lis = name.split('/')
   dname = lis[0].strip()
   rname = lis[1].strip()
   stars = str[i].a.text.strip()
   print(dname)
   print(rname)
   print(stars)
   print('\n')

