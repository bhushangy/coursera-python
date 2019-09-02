from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

#pwd = "bhushangy1999"
driver = webdriver.Firefox()


usns = []
results = {}

for i in range(1, 400):
    if i < 10:
        usns.append("1MS18IS00" + str(i))
    elif 100 > i >= 10:
        usns.append("1MS18IS0" + str(i))
    elif 100 <= i:
        usns.append("1MS18IS" + str(i))


driver.implicitly_wait(30)

driver.get('http://exam.msrit.edu')
captcha = input('enter captcha ')

for usn in usns:
    usn_ip = driver.find_element_by_css_selector('#usn')
    usn_ip.send_keys(usn)

    captcha_ip = driver.find_element_by_css_selector('#osolCatchaTxt0')
    captcha_ip.send_keys(captcha.upper())

    enter = driver.find_element_by_css_selector('.buttongo').click()

    # error check
    script = BeautifulSoup(driver.execute_script('return document.body.innerHTML'), 'html.parser')
    x = script.select('center')
    print(x)
    if len(x) != 0:
        print("holo")
        driver.back()
        continue

    name = script.find('td',class_='headingdateWhite')
    sgpa = script.find('span',class_='blue')
    print(name)
    print(sgpa)

    driver.back()
