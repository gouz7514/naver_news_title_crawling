import requests
from bs4 import BeautifulSoup

naver_url = "http://www.naver.com"

html = requests.get(naver_url).text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
news_link_list = []
news_link = soup.select('#news_cast > div.area_newstop > div > div a')
for i in range(len(news_link)):
    print(news_link[i]['href'])
    news_link_list.append(news_link[i]['href'])

f = open('naver_news_title.txt','w', encoding='utf-8')
f.write('\n'.join(news_link_list))
f.close()

# # 급상승 검색어만 추출(이건 실패함)
# searchword_list = []
# for elem in elem_list:
#     searchword_list.append(elem.get_text())
#
# # 결과 확인
# for searchword in searchword_list:
#     print(searchword)