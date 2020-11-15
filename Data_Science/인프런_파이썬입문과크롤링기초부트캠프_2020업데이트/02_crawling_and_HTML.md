# **패턴으로 실습하며 익히기: HTML 이해를 바탕으로 크롤링하기**
---  
## **크롤링 패턴 코드**  
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('크롤링할 페이지 주소')

soup = BeautifulSoup(res.content, 'html.parser')

# 필요한 데이터 추출하는 코드 넣기
mydata = soup.find('title')

# 추출한 데이터를 변수에 넣은 후, 원하는 프로그래밍
print(mydata.get_text())
```
---  
## **HTML 언어 이해를 기반으로 크롤링해보기**

### **1) h1 태그 추출 코드**  
```python
from bs4 import BeautifulSoup
html = "<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
        </html>"

soup = BeautifulSoup(html, "html.parser")

# 태그로 검색 방법
data = soup.find('h1')

print(data)
# 실행 결과
# <h1 id='title'>[1]크롤링이란?</h1>

print(data.string)
# 실행 결과
# [1] 크롤랑이란?

print(data.get_text())
# 실행 결과
# [1] 크롤링이란?
```  

### **2) p 태그 추출**
- 추출 방법  
    - `data = soup.find('p',class_='cssstyle')`
    - `data = soup.find('p', 'cssstyle')`
    - `data = soup.find('p', attrs = {'align':'center'})`
    - `data = soup.find(id='body')`  
- p 태그 추출 코드
```python
from bs4 import BeautifulSoup
html = "<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
        </html>"

soup = BeautifulSoup(html, "html.parser")

data = soup.find('p',class_='cssstyle')
print(data.sting)
# 실행 결과
# 웹페이지에서 필요한 데이터를 추출하는 것

data = soup.find('p', 'cssstyle')
print(data.sting)
# 실행 결과
# 웹페이지에서 필요한 데이터를 추출하는 것

data = soup.find('p', attrs = {'align':'center'})
print(data.string)
# 실행 결과
# 파이썬을 중심으로 다양한 웹크롤링 기술 발달

data = soup.find(id='body')
print(data.string)
# 실행 결과
# 파이썬을 중심으로 다양한 웹크롤링 기술 발달
```  
### **3) find_all() 함수 사용하기**
- find_all('태그')
    - 태그에 해당하는 모든 데이터를 추출할 수 있음
- find_all() 함수 사용법
```python
paragraph_data = soup.find_all('p')
        
for paragraph in data_data:
    print(paragraph.get_text())
```
- 모든 p 태그 추출 코드
```python
from bs4 import BeautifulSoup
html = "<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
        </html>"

soup = BeautifulSoup(html, "html.parser")

data = soup.find_all('p')
for item in data:
    print(item.string)

# 실행 결과
# 웹페이지에서 필요한 데이터를 추출하는 것
# 파이썬을 중심으로 다양한 웹크롤링 기술 발달
```