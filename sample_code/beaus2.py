from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
l = list()
sum = 0
# Retrieve all of the anchor tags
tags = soup.find_all('span')
for tag in tags:
    l.append(tag.contents)

for i in l:
    print(i)
    sum = sum + int(i[0]) #converting a list object to int object
print(sum)

#for tag in tags:
#    l.append(int(tag.contents[0]))

#print(sum(l))
