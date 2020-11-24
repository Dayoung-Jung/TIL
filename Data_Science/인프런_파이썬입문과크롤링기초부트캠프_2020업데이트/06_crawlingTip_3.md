# **크롤링 강력한 팁3 - 파이썬 문자열 함수와 함께 쓰기**

## **1. strip() 함수 사용해보기**
## **2. split() 함수 사용해보기**  

- 코드
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

section = soup.find('ul', id='dev_course_list')
titles = section.find_all('li', 'course')
for index, title in enumerate(titles):
    print(index+1, title.get_text().split('-')[-1].split('[')[0].strip())
```

- 코드 실행 결과
```
1 강사가 실제 사용하는 자동 프로그램 소개
2 필요한 프로그램 설치 시연
3 데이터를 엑셀 파일로 만들기
4 엑셀 파일 이쁘게! 이쁘게!
5 나대신 주기적으로 파이썬 프로그램 실행하기
6 파이썬으로 슬랙(slack) 메신저에 글쓰기
7 웹사이트 변경사항 주기적으로 체크해서, 메신저로 알람주기
8 네이버 API 사용해서, 블로그에 글쓰기
9 자동으로 쿠팡파트너스 API 로 가져온 상품 정보, 네이버 블로그/트위터에 홍보하기
```