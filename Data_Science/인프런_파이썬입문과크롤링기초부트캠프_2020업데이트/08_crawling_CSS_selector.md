# **CSS selector 사용해서 크롤링하기2**

## **8. CSS Selector 사용 (select_one)**
- 조건을 만족하는 가장 상위의 하나만 크롤링 됨
- 예제8 (select_one)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
item = soup.select_one('ul#dev_course_list > li.course.paid')
print(item.get_text())
```
- 예제8 실행 결과
```
(중급) - 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기 [412]
```
---
## **9. 추출한 것에서 추출하기 (find()와 select() 비교)**
- find()/select() 로 가져온 객체에는 find()/select() 함수를 사용 가능

- 예제 9-1 (select()만 사용)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('http://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('tr td')
for item in items:
    print(item.get_text())
```

- 예제 9-1 실행 결과
```
일정
커리큘럼 타이틀
난이도
5.1 ~ 6.15
나만의 엣지있는 블로그 사이트 만들기 (취미로 익히는 IT)
초급
6.16 ~ 7.31
파이썬과 데이터과학 첫걸음 (IT 기본기 익히기)
중급
```

- 예제 9-2 (find()와 select() 함께 사용)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
trs = soup.select('tr')
for tr in trs:
    tds = tr.find_all('td')
    tds_str = ''
    for td in tds:
        tds_str = tds_str + ', ' + td.get_text()
    print(tds_str[2:])
```

- 예제 9-2 실행 결과
```
일정, 커리큘럼 타이틀, 난이도
5.1 ~ 6.15, 나만의 엣지있는 블로그 사이트 만들기 (취미로 익히는 IT), 초급
6.16 ~ 7.31, 파이썬과 데이터과학 첫걸음 (IT 기본기 익히기), 중급
```