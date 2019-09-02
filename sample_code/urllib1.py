import urllib.request
import re
v = list()
fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in fhand:
    line.decode().strip()
    if re.search('^<a',line.decode().strip()):
       v = re.findall('^<a.+(http.+")',line.decode().strip())

print(v)
