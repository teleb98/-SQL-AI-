# #IMDb 사이트에서 Inception 영화에 대해서 리뷰 10개 데이터 수집 및 감성 분석 추가하고 csv 파일로 저장하기, 
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# from textblob import TextBlob

# # IMDb 리뷰 페이지 URL
# url = 'https://www.imdb.com/title/tt1375666/reviews?ref_=tt_ql_3'

# # 리뷰 데이터를 담을 데이터프레임 생성
# reviews = pd.DataFrame(columns = ['Title', 'Review', 'Polarity', 'Subjectivity'])

# # 리뷰 페이지의 개수만큼 반복
# for i in range(1, 11):
#     # 리뷰 페이지 URL
#     page_url = url + '&page=' + str(i)
#     # print(page_url)
    
#     # 리뷰 페이지를 가져옴
#     response = requests.get(page_url)
#     html = response.text.strip()
#     soup = BeautifulSoup(html, 'html5lib')
    
#     # 리뷰 데이터 추출
#     title = soup.select('h1')[0].get_text(strip=True)
#     review_list = soup.select('.text.show-more__control')
#     review_text = [tags.get_text(strip=True) for tags in review_list]
    
#     # 리뷰 데이터를 데이터프레임에 추가
#     for review in review_text:
#         blob = TextBlob(review)
#         reviews.loc[len(reviews)] = [title, review, blob.sentiment.polarity, blob.sentiment.subjectivity]

# # 리뷰 데이터를 코드가 '저장된 폴더'에 csv 파일로 저장
# reviews.to_csv(r'C:\test files\SQL AI algorithm\IMDB\imdb_reviews.csv', index=False)

# print('저장 완료')

from bs4 import BeautifulSoup
import requests
import pandas as pd
from textblob import TextBlob

# IMDb 리뷰 페이지 URL
url = 'https://www.imdb.com/title/tt1375666/reviews?ref_=tt_ql_3'

# HTML 내용을 가져옴
response = requests.get(url)
html = response.text

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 리뷰 데이터를 저장할 리스트
reviews = []

# HTML에서 리뷰 텍스트 추출
for div in soup.find_all('div', class_='text show-more__control')[:10]:
    reviews.append(div.text.strip())

# DataFrame 생성 및 감성 분석
df = pd.DataFrame({'Review': reviews})
df['Sentiment'] = df['Review'].apply(lambda review: TextBlob(review).sentiment.polarity)

# 결과를 CSV 파일로 저장
df.to_csv(r'C:\test files\SQL AI algorithm\IMDB\inception_reviews.csv', index=False)

print("리뷰 데이터가 'inception_reviews.csv' 파일에 저장되었습니다.")
