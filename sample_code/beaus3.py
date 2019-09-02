import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = 'http://python-data.dr-chuck.net/known_by_Conar.html'
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/known_by_Layah.html'
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html,"html.parser")
tag = soup('a') #list of key value pairs are thre in tag now
#print href

for i in range(count):
    link = tag[position].get('href', None)
    print('Retrieving:',tag[position])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tag = soup('a')
