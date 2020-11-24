# **바로 실전 크롤링해보기: 네이버 쇼핑 사이트 크롤링하기**

## **네이버 쇼핑 사이트 크롤링하기1**

- 크롤링 코드
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('a._popular_srch_lst_li')
for item in items:
    print(item.get_text())
```

- 코드 실행 결과
```
에어팟 프로
KF94 마스크
헤드셋
크리스마스 트리
면도기
편백나무 찜기
숏패딩
롱패딩
와플메이커
마스크
```