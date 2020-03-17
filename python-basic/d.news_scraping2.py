# %%
import time
import requests
from bs4 import BeautifulSoup

# %%
url = "https://news.naver.com/main/list.nhn"
query = "mode={0}&mid={1}&sid1={2}&date={3}&page={4}"

page = 1
date = '20200317'

news_list = []
while True:
    if page > 3:
        break

    resp = requests.get(''.join([url, '?', query]).format('LSD', 'sec', '001', date, page))
    soup = BeautifulSoup(resp.text, "html.parser")
    print(resp.status_code)

    if resp.status_code == 200:
        dl_list = soup.select("#main_content > .list_body > ul > li > dl")

        if len(dl_list) == 0:
            break

        for idx, dl in enumerate(dl_list, 1):
            links = dl.select("dt > a")
            link = links[0] if len(links) == 1 else links[1]
            news_list.append([link.text.strip(), link['href'], ""])

    page += 1
    time.sleep(0.2)

for idx, news in enumerate(news_list, 1):
    print("[{0}]. [{1}] [{2}]".format(idx, news[0], news[1]))

# %%
import random
from bs4.element import Tag, Comment, NavigableString

for news in news_list:
    interval = random.random()
    interval = 0.2 if interval < 0.2 else interval
    time.sleep(interval)
    resp2 = requests.get(news[1])

    if resp2.status_code == 200:
        soup2 = BeautifulSoup(resp2.text, "html.parser")
        contents = soup2.select_one("div#articleBodyContents")
        
        content_string = ""
        for child in contents.children:
            # print(type(child), "/", child.name)
            if type(child) == Tag and child.name != 'script':
                content_string += child.text.strip()
            elif type(child) == NavigableString:
                content_string += str(child).strip()

        news[2] = content_string

# %%
for news in news_list:
    print(news[0], news[1], news[2])
    print("*" * 10)

# %%
f = open("test.txt", "w", encoding="UTF-8")
f.write("write test...")
f.write("\n")
f.write("write test 2...")
f.write("\n")
f.write("파일 쓰기 테스트 3...")
f.close()

# %%
f= open("news-list-{0}.tsv".format(date), 'w', encoding="UTF-8")

f.write("title\tlink\tcontent\n")
for news in news_list:
    f.write('\t'.join(news))
    f.write('\n')

f.close()
print("파일 쓰기 완료")

# %%
# with open(...) as f: -> with block의 끝에서 f.close() 자동 호출
with open("news-list-{0}.tsv".format(date), 'w', encoding="UTF-8") as f:

    f.write("title\tlink\tcontent\n")
    for news in news_list:
        f.write('\t'.join(news))
        f.write('\n')

print("파일 쓰기 완료")