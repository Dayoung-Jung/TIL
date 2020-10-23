# JSP(java server page)란?

1. JSP란 HTML 코드에 JAVA 코드를 넣어 동적 웹페이지를 생성하는 웹어플리케이션 도구

    - Scriptlet : 자바 코드를 넣는 공간
    - <% ~ %> 를 이용하여 코드를 넣는다.

2. 사용자의 브라우저에 응답결과 표현 : <%= ~ %> : 표현식

3. JSP는 서블릿으로 바뀐다.

    - JSP는 서블릿으로 바뀔 것 이고, 바뀐 서블릿이 실행된다.
    - out.print(); == <%= %>

4. 실습 코드

- sum10.jsp
~~~ html
 <%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>1부터 10까지의 합</title>
</head>
<body>

	<% 
    int total = 0;
    for(int i = 1; i <= 10; i++){
        total = total + i;
    	}
	%>

1부터 10까지의 합 : <%=total %>
	
</body>
</html>
~~~

# JSP 라이프싸이클

1. _jspInit(), _jspService(), _jspDestroy()

    - _jspInit()
        - 단 한번 호출된다.
        - 서블릿의 초기화 작업을 진행
    - _jspService()
        - 클라이언트의 서비스 요청이 있을 때 호출된다.
        - 요청이 있을 때 마다 호출되므로 여러번 호출될 수 있다.
        - HTTP 요청(GET, POST 등) 을 처리하는 메서드 (doGet(), doPost() 등) 을 호출한다.
    - _jspDestroy()
        - 서블릿 객체가 더 이상 서비스를 하지 않는 경우에 메모리에서 제거되며 호출된다.
        - jspDestroy()가 호출되면 서블릿이 제거된다.
    - JSP에 변경사항이 있으면 jspDestroy() 호출 후, 다시 _jspInit(), _jspService() 순으로 실행된다.

2. JSP의 코드들은 기본적으로 서블릿의 _jspService() 메서드 안에 변환되어 들어간다.

3. JSP가 서블릿으로 만들어질 때, 알아서 만들어지는 객체 존재 = 내장 객체

4. JSP -> 서블릿으로 변환될 때
    - JSP의 HTML 코드는 서블릿에서 out.write();로 작성된다.
    - JSP의 <% 자바 코드 %>는 서블릿에서 <% %>를 제외한 내용이 그대로 작성된다.
    - JSP의 <%= %> 은 서블릿에서 out.print();로 작성된다.

5. JSP의 실행순서
    
    - 브라우저가 웹서버에 JSP에 대한 요청정보를 전달
    - 브라우저가 요청한 JSP가 최초인 경우
        - JSP를 서블릿 코드로 변환하여 java파일 생성
        - 서블릿 코드를 컴파일하여 bytecode로 변환 == class 파일 생성
        - 서블릿 클래스 로딩하고 인스턴스 생성 (인스턴스 : 객체를 소프트웨어에 실체화한 것)
    - 서블릿이 실행되어 요청을 처리하고 응답 정보를 생성

6. <%! %> : 클래스에 메서드를 선언하거나 필드를 선언할 때 Service() 메서드 바깥쪽에 해당 코드들이 만들어 질 수 있다.

7. 실습 코드
- lifecycle.jsp
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<%
	System.out.print("jspService()");
%>

<%!
	public void jspInit(){
	System.out.print("jspInit()!!!");
}
%>

<%!
	public void jspDestroy(){
	System.out.print("jspDestroy()");
}
%>

</body>
</html>
~~~


# JSP 문법

1. 스크립트 요소의 이해
    - JSP 페이지에서는 선언문(Declaration), 스크립트릿(Scriptlet), 표현식(Expression) 이라는 3가지의 스크립트 요소를 제공

2. 선언문 (Declaration)
    - 선언문 : <%! %>
    - 선언문의 문법 : <%! 문장 %>
    - 전역 변수 선언 및 메소드 선언에 사용
        - JSP 페이지 내에서 필요한 멤버변수나 메소드가 필요할 때 선언해 사용하는 요소
        - 선언된 변수는 전역 변수이므로 어느 위치에서도 참조 가능
    - Service() 메서드 밖에 코드가 작성된다.

3. 스크립트릿 (Scriptlet)
    - 스크립트릿 : <% %>
    - 스크립트릿의 문법 : <% 문장 %>
    - 가장 일반적으로 많이 쓰이는 스크립트 요소
    - 프로그래밍의 로직을 기술할 때 사용
    - 스크립트릿에서 선언된 변수는 지역 변수
        - Service() 메서드 내에서 작성된다.

4. 표현식 (Expression)
    - 표현삭 : <%= %>
    - 표현식의 문법 : <%= 문장 %>
    - JSP 페이지에서 웹 브라우저에 출력할 부분을 표현
    - 스크립트릿내에서 출력할 부분은 내장 객체인 out 객체의 print() 또는 println() 메소드를 사용해서 출력

5. 주석 (Comment)
    - JSP 페이지에서 사용할 수 있는 주석
        - HTML 주석
        - 자바 주석
        - JSP 주석
    - HTML 주석
        - < !-- 문장 -->
        - 웹 서비스 화면에 주석 내용이 보이지는 않으나, [소스 보기]를 수행하면 주석의 내용이 화면에 표시
    - JSP 주석
        - < %-- 문자 --% >
        - 웹 브라우저에 표시되지도, 소스보기를 통해 표시되지도 않음
    - 자바 주석
        - //한문장 , /* 여러 문장 */
        - 서블릿으로 실행할 때 실행되지 않는다.

6. 실습 코드
- exam1.jsp
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

id : <%=getId() %>

<%!
    String id = "u001"; //멤버변수 선언
    public String getId( ) { //메소드 선언
        return id;
    }
%>

</body>
</html>
~~~
- exam2.jsp
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	for(int i=1; i<=5; i++){
		
%>
<H<%=i %>>아름다운 한글</H<%=i %>>
<%
	}
%>
</body>
</html>
~~~

- exam3.jsp
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	for(int i=1; i<=5; i++){
		
%>
<H<%=i %>>아름다운 한글</H<%=i %>>
<%
	}
%>
</body>
</html>
~~~

# JSP 내장객체

1. JSP 내장 객체란?
    - JSP에서 개발자가 선언하지 않아도 사용할 수 있는 미리 선언된 변수
    - request, response, out, application, page, session 와 같은 변수를 내장 객체라고 한다.

2. request
    - HTML Form 요소 선택 값과 같은 사용자 입력 정보를 읽어올 때 사용
3. response
    - 사용자 요청에 대한 응답을 처리할 때 사용
4. out
    - 사용자에게 전달하기 위한 output 스트링을 처리하기 위해 사용
5. application
    - 웹 서버의 애플리케이션 처리와 관련된 정보를 참조하기 위해 사용
6. page
    - 현재 JSP 페이지에 대한 클래스 정보
7. session
    - 클라이언트 세션 정보를 처리하기 위해 사용

8. 실습 코드
- ImplicitObjects.jsp
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<% 
	StringBuffer url = request.getRequestURL();
	out.print("url :" + url.toString());
	out.print("<br>");
%>
</body>
</html>
~~~
