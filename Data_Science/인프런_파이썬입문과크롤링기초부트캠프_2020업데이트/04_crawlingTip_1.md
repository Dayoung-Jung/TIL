# **크롤링 강력한 팁1 - 크롬 브라우저 활용하기**
---
## **오픈 크롬 개발자 모드**
- Command + Alt + i (맥)
- Ctrl + Shift + i 또는 F12 (윈도우)
---
## **크롬 브라우저에서 데이터 추출**  

- 코드 작성
```python
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

titles = soup.find_all('li', 'course')
for title in titles:
    print(title.get_text())
```  

- 실행 결과
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