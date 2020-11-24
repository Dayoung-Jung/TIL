# **크롤링 강력한 팁2 - 추출한 것에서 또 추출하기**

### **1. find()로 더 크게 감싸는 HTML 태그로 추출하고**
### **2. 다시 추출된 데이터에서 find_all()로 원하는 부분을 추출**

- 예제 코드
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

section = soup.find('ul', id='dev_course_list')
titles = section.find_all('li', 'course')
for title in titles:
    print(title.get_text())
```

- 실행 결과
```
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