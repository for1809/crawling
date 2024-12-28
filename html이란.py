'''
HTML: Hyper Text Markup Language의 약자로서 웹사이트의 구조를 표시하기 위한 언어
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