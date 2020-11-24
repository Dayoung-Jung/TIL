# **CSS selector 사용해서 크롤링하기 1**

## **1. CSS Selector 사용법**
- select() 안에 태그 또는 CSS class 이름 등을 넣어주면 됨
- 결과 값은 리스트 형태로 반환됨
    - 매칭되는 첫번째 데이터만 얻고자 할 때는 select_one(), 이때는 해당 아이템 객체가 리턴
---

## **2. CSS Selector 사용 (태그 선택)**
- 예제2 (태그 선택)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('li')
for item in items:
    print(item.get_text())
```

- 예제2 실행 결과
```
(왕초보) - 클래스 소개
(왕초보) - 블로그 개발 필요한 준비물 준비하기
(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
(왕초보) - 초간단 페이지 만들어보기
(왕초보) - 이쁘게 테마 적용해보기
(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기
(초급) - 강사가 실제 사용하는 자동 프로그램 소개 [2]
(초급) - 필요한 프로그램 설치 시연 [5]
(초급) - 데이터를 엑셀 파일로 만들기 [9]
(초급) -     엑셀 파일 이쁘게! 이쁘게! [8]
(초급) -     나대신 주기적으로 파이썬 프로그램 실행하기 [7]
(초급) - 파이썬으로 슬랙(slack) 메신저에 글쓰기 [40]
(초급) - 웹사이트 변경사항 주기적으로 체크해서, 메신저로 알람주기 [12]
(초급) - 네이버 API 사용해서, 블로그에 글쓰기 [42]
(중급) - 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기 [412]
```
---

## **3. CSS Selector 사용 (하위 태그 선택)** 
- 예제 3-1 (하위 태그 선택)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('ul a')
for item in items:
    print(item.get_text())
```
- 예제 3-1 실행 결과
```
(왕초보) - 클래스 소개
(왕초보) - 블로그 개발 필요한 준비물 준비하기
(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
(왕초보) - 초간단 페이지 만들어보기
(왕초보) - 이쁘게 테마 적용해보기
(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기
(초급) - 강사가 실제 사용하는 자동 프로그램 소개 [2]
(초급) - 필요한 프로그램 설치 시연 [5]
(초급) - 데이터를 엑셀 파일로 만들기 [9]
(초급) -     엑셀 파일 이쁘게! 이쁘게! [8]
(초급) -     나대신 주기적으로 파이썬 프로그램 실행하기 [7]
(초급) - 파이썬으로 슬랙(slack) 메신저에 글쓰기 [40]
(초급) - 웹사이트 변경사항 주기적으로 체크해서, 메신저로 알람주기 [12]
(초급) - 네이버 API 사용해서, 블로그에 글쓰기 [42]
(중급) - 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기 [412]
```

- 예제 3-2 (하위 태그 선택)
    - '>'는 바로 아래 태그인 경우를 검색
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('ul > li')
for item in items:
    print(item.get_text())
```

- 예제 3-2 실행 결과
```
(왕초보) - 클래스 소개
(왕초보) - 블로그 개발 필요한 준비물 준비하기
(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
(왕초보) - 초간단 페이지 만들어보기
(왕초보) - 이쁘게 테마 적용해보기
(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기
(초급) - 강사가 실제 사용하는 자동 프로그램 소개 [2]
(초급) - 필요한 프로그램 설치 시연 [5]
(초급) - 데이터를 엑셀 파일로 만들기 [9]
(초급) -     엑셀 파일 이쁘게! 이쁘게! [8]
(초급) -     나대신 주기적으로 파이썬 프로그램 실행하기 [7]
(초급) - 파이썬으로 슬랙(slack) 메신저에 글쓰기 [40]
(초급) - 웹사이트 변경사항 주기적으로 체크해서, 메신저로 알람주기 [12]
(초급) - 네이버 API 사용해서, 블로그에 글쓰기 [42]
(중급) - 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기 [412]
```
---

## **4. CSS Selector 사용 (css class 이름으로 검색)**
- '클래스 이름'으로 검색 가능
- 예제 4 (css class 이름으로 검색)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('.course')
for item in items:
    print(item.get_text())
```

- 예제 4 실행 결과
```
(왕초보) - 클래스 소개
(왕초보) - 블로그 개발 필요한 준비물 준비하기
(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
(왕초보) - 초간단 페이지 만들어보기
(왕초보) - 이쁘게 테마 적용해보기
(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기
(초급) - 강사가 실제 사용하는 자동 프로그램 소개 [2]
(초급) - 필요한 프로그램 설치 시연 [5]
(초급) - 데이터를 엑셀 파일로 만들기 [9]
(초급) -     엑셀 파일 이쁘게! 이쁘게! [8]
(초급) -     나대신 주기적으로 파이썬 프로그램 실행하기 [7]
(초급) - 파이썬으로 슬랙(slack) 메신저에 글쓰기 [40]
(초급) - 웹사이트 변경사항 주기적으로 체크해서, 메신저로 알람주기 [12]
(초급) - 네이버 API 사용해서, 블로그에 글쓰기 [42]
(중급) - 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기 [412]
```
---
## **5. CSS Selector 사용 (id 이름으로 검색)**
- '#id 이름'으로 검색 가능
- 예제 5 (id 이름으로 검색)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('#start')
for item in items:
    print(item.get_text())
```
- 예제 5 실행 결과
```
(왕초보) - 클래스 소개
(왕초보) - 블로그 개발 필요한 준비물 준비하기
(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
(왕초보) - 초간단 페이지 만들어보기
(왕초보) - 이쁘게 테마 적용해보기
(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기
```
---
## **6. CSS Selector 사용 (태그.클래스이름1.클래스이름2. ...)**
- 클래스가 여러개인 경우 사용
- 예제 6 (태그.클래스이름1.클래스이름2. ...)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('http://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('li.course.paid')
for item in items:
    print(item.get_text())
```

- 예제 6 실행 결과
```
(중급) - 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기 [412]
```
---
## **7. CSS Selector 사용 (복합 예제)**

- 예제 7 (복합 예제)
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('ul#hobby_course_list li.course')
for item in items:
    print(item.get_text())
```

- 예제 7 실행 결과
```
(왕초보) - 클래스 소개
(왕초보) - 블로그 개발 필요한 준비물 준비하기
(왕초보) - Github pages 설정해서 블로그 첫 페이지 만들어보기
(왕초보) - 초간단 페이지 만들어보기
(왕초보) - 이쁘게 테마 적용해보기
(왕초보) - 마크다운 기초 이해하고, 실제 나만의 블로그 페이지 만들기
(왕초보) - 다양한 마크다운 기법 익혀보며, 나만의 블로그 페이지 꾸며보기
```
---
