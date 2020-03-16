# %%
import time
import requests
from bs4 import BeautifulSoup

# %%
url = "https://news.naver.com/main/list.nhn"
query = "mode={0}&mid={1}&sid1={2}&date={3}&page={4}"
# '='.join(['test', 'string', 'concat']) -> 'test=string=concat'
resp = requests.get(''.join([url, '?', query])\
               .format('LSD', 'sec', '001', '20200316', '1'))
time.sleep(0.2)
# print(resp.text)

# %%
from bs4 import BeautifulSoup

# %%
soup = BeautifulSoup(resp.text, "html.parser")

# %%
print(resp.status_code)
if resp.status_code == 200:
    dl_list = soup.select("#main_content > .list_body > ul > li > dl")

    for idx, dl in enumerate(dl_list, 1):
        links = dl.select("dt > a")
        link = None

        # if len(links) == 1:
        #     link = links[0]
        # else:
        #     link = links[1]
        link = links[0] if len(links) == 1 else links[1]

        print("[{0}]. [{1}] [{2}]".format(idx, link.text.strip(), link['href']))