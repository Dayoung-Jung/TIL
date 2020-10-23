#### **목차**

---

-   웹 서버 vs WAS
-   WAS를 사용하는 이유

#### **웹 서버 vs WAS**

---

[##_Image|kage@b9rZkL/btqIvX0p1wJ/9SK7nAFNe9IiAAskLHAC71/img.png|alignCenter|data-filename="static-vs-dynamic.png" data-origin-width="3233" data-origin-height="1262" data-ke-mobilestyle="widthContent"|웹 서버와 WAS||_##]

**1) 웹 서버**

웹 서버는 웹 클라이언트의 요청에 따라 콘텐츠를 제공하는 서버이다.

이때, 웹 서버는 **정적인 컨텐츠****(html, css, js)**를 웹 브라우저에게 제공하는 역할을 한다.

예를 들어, Apache, Nginx 등이 있다.

**2) WAS**

WAS는 웹 클라이언트의 요청에 따라 콘텐츠를 제공하는 서버이다.

이때, WAS는 DB 조회나, 어떤 로직을 처리해야 하는 **동적인 컨텐츠(asp, php, jsp)**를 웹 브라우저에게 제공하는 역할을 한다.

또한 자체적으로 웹서버의 기능도 가지고 있어서 **정적인 콘텐츠**를 처리하기도 한다.

보통 프로그램이 동작해서 얻은 결과를 보통 동적인 콘텐츠라고 말한다.

예를 들어, Tomcat, Jeus 등이 있다.

#### **WAS를 사용하는 이유**

---

[##_Image|kage@b24DDg/btqIhY1cX6T/ZmegJ1LOF3lxNprONY5se0/img.png|alignCenter|data-filename="2771214B56E9F4FE05.png" data-origin-width="900" data-origin-height="254" data-ke-mobilestyle="widthContent"|||_##]

웹 서버와 WAS 모두 서버이기 때문에, **굳이 두 개의 서버가 필요한가? 굳이 두 개로 분리해야하나?** 라는 생각이 들수도 있다.

또한 **웹 서버와 WAS를 하나의 서버로 합쳐서 실행시키는 것이 더 좋지 않을까?** 라는 생각을 할 수도 있다.

그러나 웹 서버와 WAS는 **의도적으로 분리**시켜서 사용하는 서버이다.

그 이유는 다음과 같다.

[##_Image|kage@bEFUr7/btqIh0kqFId/FdxNIbasfXUTiMBhF0m7fK/img.png|alignCenter|data-filename="blob" data-origin-width="367" data-origin-height="258" data-ke-mobilestyle="widthContent"|웹 클라이언트 - 웹 서버 - WAS 순서||_##]

**첫째, 장애 극복 기능 목적**

프로그램의 규모가 커질수록 웹 서버와 WAS를 분리시킨다.

그리고 웹 서버를 WAS 앞단에서 동작하도록 하는 경우가 많다.

그 이유는 장애 극복 기능을 위해서 이다.

**장애 극복 기능**이란, **컴퓨터 서버, 시스템, 네트워크 등에서 이상이 생겼을 때 예비 시스템으로 자동전환되는 기능**이다.

가끔 대용량 웹 애플리케이션에서 에러가 발생해 실행이 중단되는 경우다 있다.

이러한 에러를 방지하여 무중단 운영을 하기 위해 웹 서버와 WAS를 분리시킨다. 

**둘째, 서버의 부담 절감**

웹 서버를 WAS 앞단에서 동작하도록 하여, 웹 서버에서는 정적인 문서만 처리하도록 한다.

그리고 WAS는 애플리케이션의 로직만 수행하도록 기능을 분배하여 서버의 부담을 줄이기 위한 것이다.

**셋째, 보안 강화**

웹 서버를 WAS의 앞단에 배치시킴으로써, WAS의 환경설정 파일을 외부에 노출시키지 않도록 한다.

웹 서버와 WAS는 포토가 다르기 때문에, WAS에 들어오는 포트에 방화벽을 쳐서 보안을 강화할 수도 있다.

