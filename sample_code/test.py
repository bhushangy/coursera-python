import requests
from bs4 import BeautifulSoup4 as bs
result = requests.post{'http://results.rvce.edu.in/viewresult2.php',data={'usn':1RV17IS004}}
S = bs{result.content,'lxml'}
for t in s.find_all{'b'}:
    print(t.string)
