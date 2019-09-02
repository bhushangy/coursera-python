import requests
from bs4 import BeautifulSoup as bs

PARAMS = {'usn':'1RV17IS004'}

result = requests.post('http://results.rvce.edu.in/viewresult2.php',params = PARAMS)

s = bs(result.content,'lxml')
for t in s.find_all('b'):
    print(t.string)
