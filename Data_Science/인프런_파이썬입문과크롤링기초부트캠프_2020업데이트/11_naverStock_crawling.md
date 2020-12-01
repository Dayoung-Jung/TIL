# **바로 실전 크롤링해보기: 네이버 주식 사이트 크롤링하기**

## **네이버 주식 사이트 크롤링해보기1**

- 주식 인기 검색 종목 TOP10 크롤링 코드 (1) (2020.12.01 기준)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('#popularItemList > li > a')
for item in data:
    print(item.get_text())
```

- 코드 실행 결과
```
삼성전자
아시아나항공
신풍제약
셀트리온
대한항공
카카오
박셀바이오
경보제약
삼성전자우
두산중공업
```

<br>

- 주식 인기 검색 종목 TOP10 크롤링 코드 (2) (2020.12.01 기준)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('div.rgt > ul.lst_pop > li')

for item in data:
    print("지수이름:", item.find('a').get_text(), "\t","현재지수:", item.find('span').get_text())
```

- 코드 실행 결과
```
지수이름: 삼성전자 	 현재지수: 67,800
지수이름: 아시아나항공 	 현재지수: 5,720
지수이름: 신풍제약 	 현재지수: 144,000
지수이름: 셀트리온 	 현재지수: 344,000
지수이름: 경보제약 	 현재지수: 14,950
지수이름: 대한항공 	 현재지수: 26,350
지수이름: 카카오 	 현재지수: 374,500
지수이름: 박셀바이오 	 현재지수: 111,700
지수이름: 두산중공업 	 현재지수: 15,500
지수이름: 셀트리온헬스케어 	 현재지수: 126,000
```