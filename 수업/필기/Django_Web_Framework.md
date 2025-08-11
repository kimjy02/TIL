# Django Web Framework
<details>
<summary> 목차 </summary>

1. Web Application
  - 클라이언트와 서버
  - Frontend & Backend

2. Django Framework
  - 개요
  - 가상환경
  - Django Design Pattern
  - Django Project & App

3. REST API
  - 개요
  - 자원의 식별, 행위, 표현
  - 요청과 응답
  - Django URLs
    - 변수와 URL
    - APP과 URL
  - JsonResponse
</details>

## Web Application
### 개요
#### Web Application (web service) 개발
- 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정
- 다양한 디바이스(모바일, 태블릿, PC 등)에서 웹 브라우저를 통해 접근하고 사용할 수 있음

### 클라이언트와 서버
#### 웹의 동작 방식
- 우리가 컴퓨터 혹은 모바일 기기로 웹 페이지를 보게 될 때까지 무슨 일이 일어날까?

!['클라이언트-서버'](./Django/Client_Server.png)

#### 클라이언트(Client)
- 서비스를 요청하는 주체
  (웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)

#### 서버(Server)
  - 클라이언트의 요청에 응답하는 주체
    (웹 페이지, 앱을 저장하는 컴퓨터)

#### 우리가 웹 페이지를 보게 되는 과정

![우리가 웹 페이지를 보게 되는 과정](./Django/see_web_page_cycle.png)

1. 웹 브라우저(클라이언트)에서 'google.com'을 입력
2. 브라우저는 인터넷에 연결된 전세계 어딘가에 있는 구글 컴퓨터(서버)에게 'Google 홈페이지.html' 파일을 달라고 요청
3. 요청을 받은 구글 컴퓨터는 데이터 베이스에서 'Google 홈페이지.html'파일을 찾아 응답
4. 전달받은 "Google 홈페이지.html' 파일을 사람이 볼 수 있도록 웹 브라우저가 해석해주면서 사용자는 구글의 메인 페이지를 보게 됨

### Fronted & Backend
#### 웹 개발에서의 Frontend와 Backend
- Fronted(프론트엔드)
  - 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
  - > HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

- Backend(백엔드)
  - 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
  - > 서버 언어(Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등

## Framework
### Web Framework
#### '웹 서비스 개발'에는 무엇이 필요할까?
- 로그인, 로그아웃, 회원관리, 데이터베이스, 보안 등.. 너무 많은 기술들이 필요
- 하나부터 열까지 개발자가 모두 작성하는 것은 현실적으로 어려움
- 하지만 모든 걸 직접 만들 필요가 없음
- 잘 만들어진 것들을 가져와 좋은 환경에서 내 것으로 잘 사용하는 것도 능력인 시대

#### Web Framework
- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구 (개발에 필요한 기본 구조, 규칙,라이브러리 등을 제공)
