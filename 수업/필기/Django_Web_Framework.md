# Django Web Framework
<details>
<summary> 목차 </summary>

1. Web Application
  - 클라이언트와 서버
  - Frontend & Backend

주여나 피곤해 집에 가고 싶어 ai 시러시러시러시러시러시러시러

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

### Django framework
#### Django
- Python 기반의 대표적인 웹 프레임워크

#### 왜 Django를 사용할까?
- 다양성
  - Python 기반으로 소셜 미디어 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
- 확장성
  - 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
- 보안
  - 취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음
- 커뮤니티 지원
  - 개발자를 위한 지원, 문서 및 업데이터를 제공하는 활성화된 커뮤니티

#### 검증된 웹 프레임워크
- 대규모 서비스에서도 안정적인 서비스 제공
  - Spotify, Instagram, Dropbox, Delivery Hero

#### 가장 인기있는 Backend Framework
1. Laravel
2. Django
3. Spring
4. Flask
5. Express JS

#### Django를 사용해서 서버를 구현할 것

### 가상 환경
#### 가상 환경
- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 <span style='color:red'>독립적인</span> 실행 환경

#### 가상 환경이 필요한 시나리오 1
1. 한 개발자가 2개의 프로젝트(A와 B)를 진행해야 한다.
2. 프로젝트 A는 requests 패키지 버전 1을 사용해야 한다.
3. 프로젝트 B는 requests 패키지 버전 2를 사용해야 한다.
4. 하지만 파이썬 환경에서 패키지는 1개의 버전만 존재할 수 있다.
5. A와 B 프로젝트의 다른 패키지 버전 사용을 위한 <span style='color:red'>독립적인 개발 환경</span>이 필요하다.

#### 가상 환경이 필요한 시나리오 2
1. 한 개발자가 2개의 프로젝트(A와 B)를 진행해야 한ㄷ다.
2. 프로젝트 A는 water라는 패키지를 사용해야 한다.
3. 프로젝트 B는 fire라는 패키지를 사용해야 한다.
4. 하지만 파이썬 환경에서 water 패키지와 fire 패키지를 함께 사용하면 충돌이 발생하기 때문에 설치할 수 없다.
5. A와 B 프로젝트의 패키지 충돌을 피하기 위해 각각 <span style='color:red'>독립적인 개발 환경</span>이 필요하다.

#### 환경 구조 예시
![환경 구조 예시](./Django/environment_structure_example.png)

#### 1. 가상 환경 venv 생성
`$ python -m venv venv`

#### 2. 가상 환경 활성화
`$ source venv/Scripts/activate`

#### 3. 환경에 설치된 패키지 목록 확인
```bash
$ pip list
  Package       Version
  -----------   --------
  pip           23.0.1
  setuptools    58.1.0
```

#### 패키지 목록이 필요한 이유
- 만약 2명(A와 B)의 개발자가 하나의 프로젝트를 함께 개발한다고 하자.
- 팀원 A가 먼저 가상 환경을 생성 후 프로젝트를 설정하고 관련된 패키지를 설치하고 개발하다가 협업을 위해 github에 프로젝트를 push한다.
- 팀원 B는 해당 프로젝트를 clone 받고 실행해보려 하지만 실행되지 않는다.
- 팀원 A가 이 프로젝트를 위해 어떤 패키지를 설치했고, 어떤 버전을 설치했는지 A의 가상 환경 상황을 알 수 없다.
- 가상 환경에 대한 정보 즉 <span style='color:red'>패키지 목록</span>이 공유되어야 한다.

#### 의존성 패키지
- 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계
- 사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음

#### 의존성 패키지 예시
- requests 설치 후 설치되는 패키지 목록 변화 (단순히 1개만 설치되는 것이 아님)

#### 4. 의존성 패키지 목록 생성
`$ pip freeze > requirements.txt`

#### 의존성 패키지 관리의 중요성
- 개발 환경에서는 각각의 프로젝트가 사용하는 패키지와 그 버전을 정확히 관리하는 것이 중요
- **<p style='font-size:20px;'> 가상 환경 & 의존성 패키지 관리**

#### [번외] 패키지 목록 기반 설치
- 처음부터 requirements.txt를 받은 상태로 진행하는 경우, 가상환경 활성화 후 requirements.txt 기반으로 패키지 설치가 필요
(가상환경 폴더 venv는 .gitignore에 의해 공유되지 않음)
- `$ pip install -r requirements.txt`

### Django 프로젝트
#### Django 프로젝트 생성 전 루틴
```bash
# 1. 가상환경(venv) 생성
$ python -m venv venv

# 2. 가상환경 활성화
$ source venv/Scripts/activate

# 3. Django 설치
$ pip install django

# 4. 의존성 파일 생성
$ pip freeze > requirements.txt
```

#### Django 프로젝트 생성
- `$ django-admin startproject firstpjt .`

#### Django 서버 실행
- `$ python manage.py runserver`

#### 서버 확인
- 'http://127.0.0.1:8000/' 접속 후 확인

## Django Design Pattern
### 개요
#### 디자인 패턴
- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책 (공통적인 문제를 해결하는 데 쓰이는 형식화된 관행)
- > "애플리케이션의 구조는 이렇게 구성하자"라는 관행

#### MVC 디자인 패턴(Model, View, Controller)
- 애플리케이션을 구조화하는 대표적인 패턴
- ("데이터" & "사용자 인터페이스" & "비즈니스 로직"을 분리)
- > <span style='color:red'>시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해</span>
- Django에서 애플리케이션을 구조화하는 패턴
- (기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것)
- View --> Template
- Controller ---> View
  - > 단순한 명칭 변경

### Project & App
#### 프로젝트와 앱
Project
 -----------------------
|   app A     app B     |
|   -----     ------    |
|  |     |   |      |   |
|  |     |   |      |   |
|  |     |   |      |   |
|   -----     ------    |
|                       |
 -----------------------

 #### Django project
 - 애플리케이션의 집합(DB 설정, URL 연결, 전체 앱 설정 등을 처리)

#### Django application
- 독립적으로 작동하는 기능 단위 모듈
- (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

#### 만약 온라인 커뮤니티 카페를 만든다면?
1. 프로젝트
  - 카페(전체 설정 담당)

2. 앱
  - 게시글, 댓글, 회원 관리 등(DB, 인증, 화면)

#### 앱을 사용하기 위한 순서
1. 앱 생성
  - 앱의 이름은 '복수형'으로 지정하는 것을 권장
  - `$ python manage.py startapp articles`

2. 앱 등록
  - 반드시 <span style='color:red'>앱을 생성한 후에 등록</span>해야 함 (등록 후 생성은 불가능)
  ```python
  # settings.py

  INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  ]
  ```
#### 프로젝트 구조
- settings.py
  - 프로젝트의 모든 설정을 관리
- urls.py
  - 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결
- __init__.py
  - 해당 폴더를 패키지로 인식하도록 설정하는 파일
- asgi.py
  - 비동기식 웹 서버와의 연결 관련 설정
- wsgi.py
  - 웹 서버와의 연결 관련 설정
- manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

#### 앱 구조
- admin.py
  - 관리자용 페이지 설정
- models.py
  - DB와 관련된 Model을 정의
  - MTV 패턴의 M
- views.py
  - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환(url, model, template과 연계)
  - MTV의 V
- apps.py
  - 앱의 정보가 작성된 곳
- tests.py
  - 프로젝트 테스트 코드를 작성하는 곳

## REST API
### 개요
#### API(Application Programming Interface)
- 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘
- > 클라이언트 - 서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

#### API 예시
- 기상 데이터가 들어있는 기상청의 시스템
- 스마트폰의 날씨 앱, 웹 사이트의 날씨 정보 등 다양한 서비스들이 이 기상청 시스템으로부터 데이터를 요청해서 받아 감

- 날씨 데이터를 얻으려면?
  - 기상청 시스템에는 정보들을 요청하는 지정된 형식이 있음
  - 지역, 날짜, 조회할 내용들(온도, 바람 등)을 제공하는 매뉴얼

-<span style='color:red'>"이렇게 요청을 보내면, 이렇게 정보를 제공해줄 것이다"</span>라는 매뉴얼
  - 소프트웨어와 소프트웨어 간 지정된 정의(형식)으로 소통하는 수단 -> API
- > 스마트폰의 날씨 앱은 기상청에서 제공하는 API를 통해 기상청 시스템과 대화하여 매일 최신 날씨 정보를 표시할 수 있음

#### API 역할
- 예를 들어 우리 집 냉장고에 전기를 공급해야 한다고 가정해보자
- 우리는 그냥 냉장고의 플러그를 소켓에 꽂으면 제품이 작동한다.
- 중요한 것은 우리가 가전 제품에 "전기를 공급하기 위해 직접 배선을 하지 않는다"는 것이다.
- 이는 매우 위험하면서도 비효율적인 일이기 때문이다.
- > 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

#### Web API
- 웹 서버 또는 웹 브라우저를 위한 API
- 현재 웹 개발은 하나부터 열까지 직접 개발하기보다 여러 Open API들을 활용하는 추세
- 대표적인 Third Party Open API 서비스 목록
  - YOUTUBE API
  - Google Map API
  - Naver Papago API
  - Kakao Map API

#### REST(Representational State Transfer)
- API Server를 개발하기 위한 일종의 소프트웨어 설게 "방법론"
- > 모두가 API Server를 설계하는 구조가 다르니 이렇게 맞춰서 설계하는 게 어때? : "규칙X"

#### RESTful API
- REST 원리를 따르는 시스템을 RESTful하다고 부름
- <span style='color:red'>"자원을 정의"</span>하고 <span style='color:red'>"자원에 대한 주소를 지정"</span>하는 전반적인 방법을 서술
- > "각각 API 서버 구조를 작성하는 모습이 너무 다르니 어느 정도 약속을 만들어서 다같이 API 서버를 구성하자!"

#### REST API
- REST라는 설계 디자인 약속을 지켜 구현한 API

#### REST에서 자원을 사용하는 법 3가지
1. 자원의 "식별"
  - URI
2. 자원의 "행위"
  - HTTP Methods
3. 자원의 "표현"
  - JSON 데이터

### 자원의 식별
#### URI(Uniform Resource Identifier : 통합 자원 식별자)
- 인터넷에서 리소스(자원)를 식별하는 문자열
- > 가장 일반적인 URI는 웹 주소로 알려진 URL

#### URL(Uniform Resource Locator : 통합 자원 위치)
- 웹에서 주어진 리소스의 주소
- > 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속
- `http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument`
  - Scheme : `http`
  p. 91
  - Domain Name : `www.example.com`
  - Port : `80`
  - Path to the file : `/path/to/myfile.html`
  - Parameters : `?key1=value1&key2=value2`
  - Anchor : `#SomewhereInTheDocument`
