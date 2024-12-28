'''
태그	        역할	                주요 속성
<head>	    문서 정보 및 설정	    <meta>, <title>
<meta>	    메타데이터 제공	    charset, name, content
<body>	    화면에 표시될 콘텐츠	텍스트, 이미지, 링크 등
<h1>~<h6>	제목	                없음
<p>	        단락	                없음
<a>	        하이퍼링크	        href

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.naver.com/') #urlopen: url을 열고 데이터를 가져오는 함수
bsObject = BeautifulSoup(html, 'html.parser') #BeautifulSoup: HTML과 XML 문서를 파싱하는 라이브러리 파싱: 데이터를 분석해서 의미있는 구조로 변환하는 과정 여기선 title, body 등으로 분해
'''
print(bsObject) # 웹문서 전체 출력
print(bsObject.head.title) # title 태그만 출력 <title>NAVER</title>
for meta in bsObject.head.find_all('meta'): # bsObject.head: HTML 문서의 <head> 태그만 반환 find_all('meta') <head> 태그 안의 모든 <meta> 태그(인코딩 등 정보를 담고있음)를 리스트로 반환
    print(meta.get('content')) #<meta>태그의 content속성값 반환 get()은 속성이 존재하지 않을 경우 None 반환(dictionary의 get과 유사한듯)
# 태그.get(속성)
for title in bsObject.head.find_all('title'):
    print(title.get('content')) #title태그에는 content 속성이 없나보다
'''

print(bsObject.head.find('meta',{'name':'description'}))
# head 태그의 meta 태그 중 name 속성 값이 description인 것으로 한정
print(bsObject.head.find('meta',{'name':'description'}).get('content'))
# head 태그의 meta 태그 중 name 속성 값이 description인 것을 찾아 content 속성을 가져옴
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
