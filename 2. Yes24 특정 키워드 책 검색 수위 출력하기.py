from urllib.request import urlopen
from bs4 import BeautifulSoup

keyword = 'opencv'
search_book_name = '알짜배기 예제로 배우는 OpenCV'

html = urlopen(f'https://www.yes24.com/Product/Search?domain=ALL&query={keyword}')
bsObject = BeautifulSoup(html, 'html.parser')

books = bsObject.find_all('div', class_='info_row info_name')

find_index = []
book_names = []
types = []
for i, book in enumerate(books):
    data = list(book.children)
    is_used = data[1].get_text()
    book_name = data[3].get_text()

    if search_book_name in book_name and '[중고도서]'!= is_used:
        find_index.append(i + 1)
        book_names.append(book_name)
        types.append(is_used)

for i,type,book in zip(find_index, types, book_names):
    print(i, type, book)