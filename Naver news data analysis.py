#네이버 뉴스 기사에 검색어 키워드 '아이브', '뉴진스'로 기간은 '2023.1.1 ~ 2023.3.30` 까지로 설정하여 검색하고 검색어가 포함된 뉴스 기사 제목과 링크를 출력하는 코드 작성해줘
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# 검색어와 날짜 설정
keywords = ['아이브', '뉴진스']
start_date = '2023.01.01'
end_date = '2023.03.30'

for keyword in keywords:
    # 검색어 인코딩
    encoded_keyword = quote(keyword)

    # 네이버 뉴스 검색 URL 생성
    url = f"https://search.naver.com/search.naver?where=news&query={encoded_keyword}&pd=3&ds={start_date}&de={end_date}"

    # HTTP 요청
    response = requests.get(url)
    html = response.text

    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 뉴스 기사 제목과 링크 추출
    for item in soup.find_all('a', class_="news_tit"):
        title = item.get('title')
        link = item.get('href')
        print(f"제목: {title}\n링크: {link}\n")

# 주의: 이 코드는 네이버 뉴스 검색 결과 페이지의 구조에 의존하므로, 페이지 구조가 변경되면 작동하지 않을 수 있습니다.
