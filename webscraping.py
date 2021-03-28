
import requests
webpage = requests.get("https://www.daangn.com/hot_articles")
print(webpage.text)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(webpage.content, "html.parser")
# print(soup)

#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.naver.com")
#
# bsObject = BeautifulSoup(html, "html.parser")
#
#
# print(bsObject) # 웹 문서 전체가 출력됩니다.



