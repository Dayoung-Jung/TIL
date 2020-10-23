#### **목차**

---

-   HTML의 개념
-   HTML의 기본 구조
-   HTML의 요소(element) 구조

#### **HTML의 개념**

---

**HTML**(**H**yper**t**ext**M**arkup**L**anguage)은 **웹 페이지**를 **표현**하는 데 사용되는 **마크업 언어**이다.

좀 더 자세히 말하면, 웹브라우저가 HTML의 문법을 해석해서 화면에 웹페이지를보여주는 것이다.

**HTML**은 주로 **웹페이지**에서 '무엇을 어디에 배치할지'와 같이 **구조화**하는 데 사용된다.

쉽게 말해서, 인테리어를 한다고 가정하면 방 하나가 웹 페이지이고 가구들을 배치하는 데 사용되는 것이 HTML이다.

(나중에 포스팅할 CSS는 배치된 가구들의 디자인이라고 이해하면 된다.)

#### **HTML의 기본 구조**

---

**1) HTML의 기본 구조**

[##_Image|kage@B0U0x/btqIM7Q65c9/Ko5pRnEAD1nsKYsKTEjJak/img.png|alignCenter|data-filename="다운로드.png" data-origin-width="385" data-origin-height="336" data-ke-mobilestyle="widthContent"|HTML의 기본 구조||_##]

HTML은 기본적으로 다음과 같음 구조를 가지고 있다.

-   **<html>**
-   **<head>**
-   **<body>**

가장 중요한 **웹페이지는 표현하는 영역은 <body>**이다.

**2) 각 구조들에 대한 설명**

**<html>**은 웹 페이지의 시작과 끝을 알리는 역할이다.

그러므로 시작과 끝에 배치되어 있어야한다. 이때 시작 자리에 <html>가 있고, 마지막 자리에 </html> 가 있다.

또한 HTML로 작성된 모든 내용은 <html>과 </html>의 사이에 있어야 한다.

**<head>**은 여러 설정들(정보들)이 모여 있는 영역이다.

예를 들어, 인코딩은 무엇인지, 제목은 무엇인지, 콘텐츠 타입은 무엇인지 등에 관한 것들이 모여있다.

그러므로 웹 페이지를 표현하는 영역은 아니다.

<head> 영역 안에는 <meta>, <style>, <title> 등이 있으며, 이때 <meta>가 인코딩, 콘텐츠 타입 등을 표시한다.

<style>은 CSS와 관련된 것이 표시되며, 사용될 수도 있고 사용되지 않을 수도 있는 부분이다.

<title>은 웹 페이지의 제목을 나타낸다.

**<body> **는 웹 페이지를 표현하는 데 사용되는 영역이다.

즉 화면에 보여지는 부분이다.

이 영역 안에는 다양한 태그들을 넣을 수 있으며 배치할 수 있다.

그렇게 배치되는 것이 바로 웹 페이지가 구조화 되는 것이다.

**3) VS Code로 보는 HTML 구조**

[##_Image|kage@v8jx3/btqIX3eOCYP/OkmZzfpKt1FKFC7OduPkR0/img.png|alignCenter|data-origin-width="0" data-origin-height="0" data-ke-mobilestyle="widthContent"|||_##]

Visual Studio Code을 통해 HTML 문서를 생성하면 가장 먼저 보이는 것이 위 사진이다.

앞에서 언급 했던것과 같이, 우선 **<html>과 </html>**이 맨 윗줄과 아래줄에 배치됨으로써 **문서의 시작과 끝**을 나타낸다.

그 다음으로 **<head>와 </head>** 로 감싸져 있는 영역이 <head>영역이다.

현재 <head> 안에 <meta>와 <title>이 있는 것을 볼 수 있다.

<style>은 아직 사용되지 않아도 되서 없는 것이다.

마지막으로 **<body>와 </body>**로 감싸져 있는 영역이 <body> 영역이다.

여러 태그들이 들어가는 영역이며, 웹 페이지를 표현할 때 주로 사용되는 공간이기도 하다.

#### **HTML의 요소(element) 구조**

---

**1) 요소(element) 란?**

요소(element)는 보통 <body>영역에 배치된다.

element들의 배치에 따라 웹 페이지가 구조화되며 표현된다.

**2) 요소(element)의 구조 **

[##_Image|kage@5z9MS/btqIM65NfA2/be185SVBXTayK3mP0GQEfK/img.jpg|alignCenter|data-filename="images.jpg" data-origin-width="300" data-origin-height="168" data-ke-mobilestyle="widthContent"|element 예시 (1)||_##]

**element**는 **태그(tag)**와 **내용(contents)**로 구성되어 있다.

tag는 contents에 효과를 주는 역할이며, 종류에는 링크 태그, p태그, 이미지 태그 등이 있다.

tag를 작성할 때는 반드시, contents** 시작부분에 여는 태그 <???>**를 쓰고 **끝 부분에 닫는 태그 </???>**를 써야한다.

그러므로 element의 구조는 항상 **「 <태그> 콘텐츠 </태그> 」** 이다.

[##_Image|kage@M3qDv/btqIS5LuHh1/KlbcK1cX0IQJWK0kBYOc41/img.png|alignCenter|data-filename="images.png" data-origin-width="335" data-origin-height="150" data-ke-mobilestyle="widthContent"|element 예시 (2)||_##]

element 들 중에 속성을 가지는 element도 있다.

이때 속성이란, element에 추가적인 내용을 담고 싶을 때 사용하는 것이다.

속성에는 class, id 등이 있다.

속성을 사용할 때는 **「 속성명 = (" 또는 ' 로 감싼) 속성값 」 **의 구조로 작성해야한다.

**3) 요소(element) 예시 **

[##_Image|kage@xdOp6/btqILLtYLFk/StvsU6xy0CPIVC32tfcwP0/img.png|alignCenter|data-filename="2020-09-16 (14).png" data-origin-width="1920" data-origin-height="1080" data-ke-mobilestyle="widthContent"|VS Code 이용||_##]

**노란색 부분**은 요소는 아니지만, 알고 넘어가면 좋을 것 같아서 추가한 내용이다.

왼쪽에 있는 <title> 과 </title> 사이에 '페이지 이름'이란 글자를 적으니까, 오른쪽의 페이지 이름이 '페이지 이름'이 된 것을 확인할 수 있다.

이처럼 <title> 과 </title> 사이에 적은 내용이 제목이 되어서, 페이지의 이름이 되는 것이다.

**파란색 부분**은 p태그를 통해 hello world를 웹 페이지에 표현한 것이다.

또한 링크 태그를 이용해서, 내 블로그로 들어올 수 있는 링크를 웹페이지에 표현한 것이다.
