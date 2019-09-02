import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = 'http://exam.msrit.edu/' # enter url
html = urllib.request.urlopen(url).read() #import url and >read() reads
soup = BeautifulSoup(html,"html.parser") #telling beautiful soup to parse it and cleans ot up and returns an object

tag = soup.find('td',class_='headingdate')
#v = tag[0].contents
print(tag.a.text)


##to retrieve all anchor tags
#tags = soup('a')
#for tag in tags: #here tags is a dictionary.... .get() is a method that retheives values based on key name passes here 'href'
#    print(tag.get('href',None))
