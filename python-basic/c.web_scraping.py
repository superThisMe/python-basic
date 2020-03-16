#%%
# import urllib.request
from urllib import request # urllib 표준 모듈에서 request 객체 import

# %%
google = request.urlopen("http://developers.google.com")
html = google.read().decode('utf-8')
print(html)

# %%
import requests

# %%
daum = requests.get("http://www.daum.net")
print(daum.status_code)
print(daum.text)

# %%
naver = requests.get("http://www.naver.net")
print(naver.status_code)
print(naver.text)

#%%
from selenium import webdriver

# %%
browser = webdriver.Chrome(r'C:\workspace\dev-tools\selenium-drivers\chromedriver.exe')

# %%
browser.get("http://python.org")

# %%
menu = browser.find_elements_by_css_selector('#top ul.menu li')

pypi = None # None == null
for m in menu: # for (변수 : 목록)
    if m.text == 'PyPI':
        pypi = m


# %%
pypi.click()

# %%
browser.quit()

#%%
import time

# %%
browser = webdriver.Chrome(r'C:\workspace\dev-tools\selenium-drivers\chromedriver.exe')
time.sleep(1) # 1초간 실행 중지

browser.get("http://www.naver.com")
time.sleep(1)

# %%
ranks = browser.find_elements_by_css_selector("#NM_RTK_VIEW_list_wrap ul li a span.ah_r")
keywords = browser.find_elements_by_css_selector("#NM_RTK_VIEW_list_wrap ul li a span.ah_k")

# %%
# type(ranks) # ranks의 자료형

# indices = range(len(ranks)) # len : 요소 갯수, range: 1 ~ n까지의 수열
# for index in indices:

# zip( (1, 2, 3), (a, b, c) ) -> (1, a), (2, b), (3, c) 
for rank, keyword in zip(ranks, keywords):
    print("[%s]. %s" % \
          (rank.get_attribute("innerText"), \
           keyword.get_attribute('innerText')))

for rank, keyword in zip(ranks, keywords):
    print("[{0}]. {1}".format(\
            rank.get_attribute("innerText"), \
            keyword.get_attribute('innerText')))

#%%
browser.quit()

# %%
import requests
from bs4 import BeautifulSoup

# %%
resp = requests.get("https://www.nate.com")

# %%
print( resp.status_code )
if resp.status_code == 200:
    # print( resp.text )
    # 응답 html Parsing -> DOM Tree 및 관련 정보로 구성된 객체 생성
    soup = BeautifulSoup(resp.text, "html.parser")
    # print (soup.prettify())

    menus = soup.select("#divGnb > ul > li > a")

    # enumerate([a, b, c]) -> (1, a), (2, b), (3, c)
    for idx, menu in enumerate(menus, 1):
        print("[{0}]. {1}".format(idx, menu.get_text()))

# %%
