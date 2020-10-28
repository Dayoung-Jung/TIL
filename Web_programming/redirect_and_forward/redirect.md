# **리다이렉트(redirect)**

## **학습목표**
- 리다이렉트를 이해한다.
- 리다이렉트를 사용할 수 있다.

## **핵심개념**
- HttpServletResponse
- sendRedirect()  

---  
<br>

## **리다이렉트(redirect)**
- 리다이렉트는 http프로토콜로 정해진 규칙이다.
- 서버는 클라이언트로부터 요청을 받은 후, 클라이언트에게 특정 URL로 이동하라고 요청할 수 있다. 이를 리다이렉트라고 한다.
- 서버에는 클라이언트에게 응답으로 상태코드를 302와 함께 이동할 URL정보를 Location 헤더(Header)에 담아 전송한다. 클라이언트는 서버로 부터 받은 상태값이 302이면 Location 헤더값으로 재요청을 보내게 된다. 이때 브라우저의 주소창은 전송받은 URL로 바뀌게 된다.
- 서블릿이나 jsp는 redirect하기 위해서 HttpServletResponse가 가지고 있는 sendRedirect() 메소드를 사용한다.  

<br>

## **redirect 실습**
- redirect01.jsp, redirect02.jsp 파일을 작성
- 웹 브라우저가 redirect01.jsp 을 요청
- redirect01은 redirect02.jsp로 리다이렉팅하는 로직이 실행되도록 함
- 결과 확인  

> redirect01.jsp
```java
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%
	response.sendRedirect("redirect02.jsp");
%>
```  

> redirect02.jsp
```java
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	redirect된 페이지 입니다^^
</body>
</html>
```  

<br>

## **브라우저에서 리다이렉트 확인**
- 크롭에서 우측버튼을 누르고 검사를 선택한 후 Network탭을 선택한다.
- redirect01.jsp를 실행하면 서버로 부터 응답코드로 302를 받는 것을 알 수 있다.  

<br>

## **예제 동작 설명**
![이미지](https://cphinf.pstatic.net/mooc/20180127_5/1517046342330PRbSX_PNG/2_4_1_redirect__.PNG)  
1. 클라이언트가 redirect01.jsp 를 서버에게 요청
2. 서버는 `response.sendRedirect("redirect02.jsp");` 를 통해, 클라이언트에게 redirect02로 리다이렉트 요청 (LoCation헤더 값: redirect02.jsp)
3. 클라이언트는 서버의 리다이렉트 요청을 받고 redirect02.jsp를 요청
4. 서버는 redirect02 결과를 클라이언트에게 전달 및 출력
5. 클라이언트(브라우저)의 주소창의 URL 주소는 redirect02.jsp로 바뀜




