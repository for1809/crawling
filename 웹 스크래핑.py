'''
HTML: Hyper Text Markup Language의 약자로서 웹사이트의 구조를 표시하기 위한 언어
태그	        역할	                주요 속성
<head>	    문서 정보 및 설정	    <meta>, <title>
<meta>	    메타데이터 제공	    charset, name, content
<body>	    화면에 표시될 콘텐츠	텍스트, 이미지, 링크 등
<h1>~<h6>	제목	                없음
<p>	        단락	                없음
<a>	        하이퍼링크	        href

HTTP: Hyper Text Transfer Protocol
서버와 클라이언트간의 웹 데이터 송수신을 위한 규약
python은 urlopen 함수를 이용해서  서버에 http request를 전송함

from urllib.request import urlopen
url = 'http://localhost:63342/crawling/test.html?_ijt=rmbjqk7duvlell21p3ngnrg1vm'
html = urlopen(url).read().decode()
print(html) # url의 html 문서를 문자열로 출력
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser') # 보기 편하게 파싱
print(soup)
list_body = soup.find_all('body') #바디 태그만 추출
print(list_body)
list_h1 = soup.find_all('h1')
print(list_h1)
for tag in list_h1:
    print(tag.get_text()) # 각 태그에서 텍스트만 추출해서 출력
'''
# 웹사이트에서 환율을 가져와 주어진 원화를 현재 환율로 계산하여 출력하기
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Edge()
driver.get('https://finance.daum.net/exchanges')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
lst = soup.find_all('span')
for i, tag in enumerate(lst):
    print(i, tag.get_text())
currency = ['USD', 'JPY100', 'CNY', 'EUR', 'GBP']
exchanges = {}
for i, c in enumerate(currency):
    l = lst[2 * i + 87]
    exchanges[c] = float(l.get_text().split()[0].replace(',', ''))

def convert(cur, won):
    if cur == 'JPY100':
        return won * 100/exchanges[cur]
    return won/exchanges[cur]
test1 = convert('USD', 1470000)
print(test1)
'''

태그 구조
<태그이름(시작태그)> 내용 </태그이름(종료태그)> ex) <head> ~~~ </head>
<태그이름 속성 = '속성값'> 내용 </태그이름> ex) <meta(태그) name(속성) = 'Referrer'(속성값) content(속성) = 'IE=edge'(속성값)>
속성(attribute): 태그의 추가적인 정보, 여러 개 부여 가능, 없어도 상관 X
<meta>는 종료태그를 사용하지 않음!
내용: 텍스트나 태그를 포함, 없어도 상관 X
부모태그: 안은문장 자식태그: 안긴문장
예시
<head>
    <script 속성 = '속성값></script>
        <?태그></?태그>
</head>
head: 부모태그
script: 자식태그이자 부모태그
?: script의 자식태그

HTML 문서 구조
<!DOCTYPE html> 이 문서는 html5로 작성됨 문서 버전
<html>
    <head>
        <웹사이트 제목, 설명, 메타태그 등 부가적인 정보>
    </head>
    <body>
        <실제로 화면에 표시되는 내용>
    </body>
</html>
주석: !--을 사용해 표현 파이썬의 #이랑 같은 역할

'''