#### **목차**

---

-   URL
-   HTTP
-   IP 주소
-   도메인 주소
-   포트 주소

#### **URL**

---

**1) URL 이란?**

URL은 웹상에서 문서, 이미지, 동영상 등의 **자원들의 위치를 나타내는 주소**이다.

쉽게 말해서, **웹 페이지를 찾기 위한 주소**를 말한다.

예를 들어,

구글 URL →[https://www.google.co.kr/](https://www.google.co.kr/)

네이버URL →[https://www.naver.com/](https://www.naver.com/)

티스토리 URL → [https://www.tistory.com/](https://www.tistory.com/)

이다.

**2) URL의 구조**

URL은 크게 3가지로 구성되어 있다.

**첫 번째, 프로토콜 종류**

**두 번째, 자원이 있는 서버의 IP 주소, 도메인 주소, 포트 주소**

**세 번째, 자원의 위치**

그러므로 URL 은 보통 " **프로토콜** **// IP 주소 or 도메인 주소 or 포트 주소 /** **자원 위치** " 의 형식을 가진다.

예를 들어, 나무위키의 URL 내용 페이지에 대한 URL을 가져와 구조를 분석하면 다음과 같다.

<table style="border-collapse: collapse; width: 100%; height: 56px;" border="1"><tbody><tr style="height: 16px;"><td style="width: 13.3721%; height: 16px; text-align: center;">&nbsp;URL</td><td style="width: 86.6281%; height: 16px; text-align: center;" colspan="5"><u><a href="https://ko.wikipedia.org/wiki/URL">https://ko.wikipedia.org/wiki/URL</a></u></td></tr><tr style="height: 20px;"><td style="width: 13.3721%; height: 40px; text-align: center;" rowspan="2">구조</td><td style="width: 19.9613%; height: 20px; text-align: center;">https</td><td style="width: 7.48056%; height: 20px; text-align: center;">://</td><td style="width: 30.8528%; height: 20px; text-align: center;">ko.wikipedia.org</td><td style="width: 11.6667%; height: 20px; text-align: center;">/</td><td style="width: 16.6667%; height: 20px; text-align: center;">wiki/URL</td></tr><tr style="height: 20px;"><td style="width: 19.9613%; height: 20px; text-align: center;">프로토콜</td><td style="width: 7.48056%; height: 20px; text-align: center;">&nbsp;</td><td style="width: 30.8528%; height: 20px; text-align: center;">도메인 주소</td><td style="width: 11.6667%; height: 20px; text-align: center;">&nbsp;</td><td style="width: 16.6667%; height: 20px; text-align: center;">자원 위치&nbsp;</td></tr></tbody></table>

#### **HTTP**

---

[##_Image|kage@m8jC9/btqIqnkRVTW/d8Ez0lT64YoYTwSLZU7KHK/img.png|alignCenter|data-filename="다운로드 (1).png" data-origin-width="1280" data-origin-height="556" data-ke-mobilestyle="widthContent"|||_##]

**1) http 란?** 

http는 **서버와 클라이언트가 인터넷 상에서 데이터를 주고받기 위한 프로토콜****(protocol)**이다.

http는 어떤 종류의 데이터도 전송할 수 있도록 설계되어 있다.

예를 들어 이미지, 동영상, 오디오, 텍스트 문서 등 종류를 가리지 않고 전송할 수 있다.

**2) http의 작동 방식**

http는 **서버****/****클라이언트 모델**을 따른다.

**클라이언트가 서버에게 요청**을 보내면, **서버는 클라이언트에게 응답**을 보낸다.

http는 **무상태 프로토콜**이며, **stateless(****무상태)** **방식**을 따른다.

**stateless(무상태)** **방식**은, 간단히 말하면 **서버가 여러 클라이언트들을 구별할 수 없다는 것**이다.

예를 들어, 클라이언트가 서버에게 요청을 보내고, 서버가 응답한 후 연결이 끊겼다고 가정하자.

그 후에 똑같은 클라이언트가 또다시 서버에게 요청을 했을 때, 서버는 그 클라이언트가 아까의 클라이언트인지 아닌지 구별할 수 없다.

이것이 stateless(무상태) 방식이다.

**3) stateless(무상태)****방식의 장·단점**

**장점**

\- 불특정 다수를 대상으로 하는 서비스에 적합

\- 클라이언트와 서버가 최대 연결 수 보다 훨씬 많은 요청과 응답을 처리할 수 있다.

**단점**

\- 연결이 끊어진 후에는 클라이언트가 이전에 무엇을 했는지 알 수 없다.

(이러한 단점을 보완하기 위해서 cookie라는 기술이 등장한다.)

#### **IP 주소**

---

IP 주소 (Internet Protocol address, IP address)는 **컴퓨터 네트워크 상에서 각 장치들의 고유 번호**이다.

쉽게 말하면, 장치들의 전화번호라고 생각하면 된다.

IP 주소의 형식은 예를 들어, ****[2606:4700:4700:0000:0000:0000:0000:1111](https://namu.wiki/w/Cloudflare#s-3.4)****와 같다.

이러한 **번호들의 나열**이 각 **장치들의 고유한 주소**인 것이다.

각각의 장치들은 IP 주소를 이용하여 데이터를 전송하기도 전달받기도 한다.

하지만 IP 주소 형식은 외우거나 구별하기 어렵기 때문에, **DNS를 통해** 구별하기 쉬운 **도메인 주소로 변환**된다.

#### **도메인 주소**

---

**도메인 주소**는 외우거나 식별하기 **어려운 IP 주소**(예:240.10.20.1)를 example.com 처럼 기억하기 **쉽게 만들어주는** **네트워크 호스트 이름을 의미**한다.

예를 들어, IP 주소와 도메인 주소를 비교하면 다음과 같다.

<table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr><td style="width: 50%; text-align: center;">IP 주소</td><td style="width: 50%; text-align: center;">도메인 주소</td></tr><tr><td style="width: 50%; text-align: center;"><span style="color: #666666;">115.68.24.88</span></td><td style="width: 50%; text-align: center;"><span style="color: #666666;">opentutorials.org</span></td></tr><tr><td style="width: 50%; text-align: center;"><span style="color: #666666;">220.95.233.172</span></td><td style="width: 50%; text-align: center;"><span style="color: #666666;">naver.com</span></td></tr><tr><td style="width: 50%; text-align: center;"><span style="color: #666666;">114.108.157.19</span></td><td style="width: 50%; text-align: center;"><span style="color: #666666;">daum.net</span></td></tr></tbody></table>

#### **포트 주소**

---

**1) 포트 주소란?**

**포트 주소**는 소프트웨어에서는 **네트워크 서비스****나 특정 프로세스****를 식별**하는 논리 단위이다.

포트는 **번호로 구별**되며 이 번호를**포트 번호**라고 한다. 포트 번호는 IP 주소와 함께 쓰여 해당하는 프로토콜에 의해 사용된다.

예를 들어, **ftp://000.000.000.000:21** 라는 URL 에서 **맨 마지막에 있는 21이 포트 번호**이다.

**2) 웹(WWW)의 포트 번호**

위에서 언급했듯이, 각각의 네트워크 서비스에는 고유 포트 번호가 존재한다.

**웹(WWW) 의 포트 번호는 80**이다.

다음은 포트 번호의 예시이다.

-   20 :FTP(data)
-   21 : FTP(제어)
-   22 :SSH
-   23 :텔넷
-   53 :DNS
-   80 :월드 와이드 웹,HTTP
-   119 :NNTP
-   443 :TLS/SSL방식의 HTTP

