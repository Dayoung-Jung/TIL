# **바로 실전 크롤링해보기: 네이버 쇼핑 사이트 크롤링하기**

## **네이버 쇼핑 사이트 크롤링하기1**

### **1) 인강 코드**
- 인기 검색어 TOP10 크롤링 코드 (2020.11.30 기준)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('#popular_srch_lst > li > span.txt')
for item in data:
    print(item.get_text())
```

- 코드 실행 결과
```
크리스마스 트리
롱패딩
면도기
헤드셋
KF94 마스크
가습기
에어팟 프로
어그 슬리퍼
숏패딩
여성 롱패딩
```

<br>

### **2) 스스로 해 본 코드**
- 인기 검색어 TOP10 크롤링 코드 (2020.11.30 기준)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('span.txt')
for index,item in enumerate(items):
    print(index+1, '위', item.get_text())
```

- 코드 실행 결과
```
1 위 크리스마스 트리
2 위 롱패딩
3 위 면도기
4 위 헤드셋
5 위 KF94 마스크
6 위 가습기
7 위 에어팟 프로
8 위 어그 슬리퍼
9 위 숏패딩
10 위 여성 롱패딩
```




