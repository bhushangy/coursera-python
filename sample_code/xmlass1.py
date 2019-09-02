import xml.etree.ElementTree as ET
from urllib.request import urlopen
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx)
data = html.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count') #search for all tags with name count and return a list


l =list()
for i in counts:
    l.append(int(i.text))
print(sum(l))


#stuff = ET.fromstring(str)
