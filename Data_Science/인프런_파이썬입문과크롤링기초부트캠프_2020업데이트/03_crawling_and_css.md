# **패턴으로 실습하며 익히기: HTML/CSS 이해를 바탕으로 크롤링하기**
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
## **HTML/CSS 언어 이해를 기반으로 크롤링해보기**

```python
data = soup.find('h3', 'tit_view')
print(data.get_text())
```

```python
data = soup.find('span', 'txt_info')
print(data.get_text())
```

```python
data = soup.find_all('span', 'txt_info')
for item in data:
    print(data.get_text())
```

```python
data = soup.find('span', 'txt_info')
print(data[1].get_text())
```

```python
data = soup.find('div', 'layer_util layer_summary')
print(data.get_text())
```