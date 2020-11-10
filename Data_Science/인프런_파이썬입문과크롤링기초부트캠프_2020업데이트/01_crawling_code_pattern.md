# **패턴으로 실습하며 익히기: 크롤링 코드 패턴으로 익히기1**
---  

## **크롤링 핵심 코드 패턴으로 이해하기**  

```python
import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.jtbc.joins.com/html/165/NB11978165.html')
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())

# 실행 결과 
# "코로나19 예방 효과 90%"…방역당국 "백신 개발되면 국내 접종은 내년 하반기쯤" | JTBC 뉴스
```  

1) 라이브러리 임포트
```python
import requests
from bs4 import BeautifulSoup
```  

2) 웹 페이지 가져오기
```python
res = requests.get('http://news.jtbc.joins.com/html/165/NB11978165.html')
```  

3) 웹 페이지 파싱하기
```python
soup = BeautifulSoup(res.content, 'html.parser')
```  

4) 필요한 데이터 추출하기
```python
mydata = soup.find('title')
```

5) 추출한 데이터 활용하기
```python
print(mydata.get_text())
```  

---
## **필요 라이브러리**
- requests
    - 웹 페이지 가져오기 라이브러리
- bs4 (BeautifulSoup)
    - 웹 페이지 분석 (크롤링)라이브러리  

---
## **1. 라이브러리 임포트(import)**
- 필요 라이브러리 
    - requests
        - 웹 페이지 가져오기 라이브러리
    - bs4 (BeautifulSoup)
        - 웹 페이지 분석 (크롤링)라이브러리  

```python
import requests
from bs4 import BeautifulSoup
```
---
## **2. 웹 페이지 가져오기**
- res.content 확인해보기
```python
res = requests.get('http://news.jtbc.joins.com/html/165/NB11978165.html')
```
---
## **3. 웹페이지 파싱하기**
- 파싱(parsing) 이란?
    - 문자열의 의미 분석
- soup에 HTML 파일을 파싱한 정보가 들어간다.
```python
soup = BeautifulSoup(res.content, 'html.parser')
```
---
## **4. 필요한 데이터 추출하기**
- soup.find() 함수로 원하는 부분을 지정
- 변수.get_text() 함수로 추출한 부분을 가져올 수 있음
```python
mydata = soup.find('title')
print(mydata.get_text())
```
