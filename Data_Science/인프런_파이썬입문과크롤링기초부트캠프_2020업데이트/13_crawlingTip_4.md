# **여러 페이지 한번에 크롤링하는 기법(2020 업데이트)**

## **HTTP response code**
- HTTP 라는 프로토콜 규격에 따라서, 응답 데이터에 응답 코드(response code)를 넣어서 보내게 됨
    - requests 라이브러리의 경우, requests.get()의 리턴변수.status_code 에서 응답 코드를 확인할 수 있음
    - HTTP 규격에 따라 응답 코드가 200인 경우는 정상 응답, 그렇지 않으면 무언가 문제가 있다는 뜻
        - 특정 페이지 요청 후, 응답 코드가 200이 아니면, 특정 페이지가 없는 경우 (또는 결과적으로는 문제가 있는 경우)라고 인지 할 수 있음

- 코드 예제
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/xxx')
if res.status_code != 200:
    print("페이지 없음")
else:
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('h4.card-text')
    for item in data:
        print(item.get_text())
```

- 코드 실행 결과
```
페이지 없음
```
---


