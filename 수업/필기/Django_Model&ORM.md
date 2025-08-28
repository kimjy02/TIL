# Django Model & ORM
<details>
<summary> 목차 </summary>

1. Model

2. Migrations

3. Admin site

4. ORM
  - QuerySet API
  - QuerySet API 실습
    - CRUD

5. Django Serializer
  - 개요
  - serializer class
  - CRUD with ModelSerializer

</details>

## 1. Model
#### Model을 통한 DB(데이터베이스) 관리
![Model을 통한 DB 관리](./Django/Manage_DB_for_Model.png)

#### Django Model
  - DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
    - > 테이블 구조를 설계하는 **청사진(blueprint)**

#### model 클래스 작성
```python
# articles/models.py

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```

#### model 클래스 살펴보기
- 작성한 모델 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦

  ![작성한 모델 클래스로 DB에 테이블 구조 만들기](./Django/Make_DB_for_model_class.png)

- `django.db.models` 모듈의 Model이라는 부모 클래스를 상속받음
- Model은 model에 관련된 모든 코드가 이미 작성되어 있는 클래스
- > 개발자는 가장 중요한 <span style='color:red'>테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록</span> 하기 위한 것(상속을 활용한 프레임워크의 기능 제공)

1. 클래스 변수명
  - 테이블의 각 "필드(열) 이름"

    ![클래스 변수명](./Django/Model_class_name.png)

2. model Field 클래스
  - 테이블 필드의 "데이터 타입"

    ![model Field 클래스](./Django/Model_Field_class.png)

3. model Field 클래스의 키워드 인자(필드 옵션)
  - 테이블 필드의 "제약조건" 관련 설정

    ![model Field 클래스의 키워드 인자](./Django/Model_Field_class_Keyword_para.png)

#### 제약 조건
- 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
- > ex) 숫자만 저장되도록, 문자가 100자까지만 저장되도록 하는 등

## 2. Migrations
#### Migrations
  - model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

#### Migrations 과정
![Migrations 과정](./Django/Migrations_cycle.png)

#### Migrations 핵심 명령어 2가지
1. `$ python manage.py makemigrations`
  - model class를 기반으로 최종 설계도(migration) 작성

2. `$ python manage.py migrate`
  - 최종 설계도를 DB에 전달하여 반영

#### migrate 후 DB 내에 생성된 테이블 확인
- Article 모델 클래스로 만들어진 articles_article 테이블

### 추가 Migrations
#### 이미 생성된 테이블에 필드를 추가해야 한다면?
![생성된 테이블에 필드 추가?](./Django/table_add_field.png)

#### 추가 모델 필드 작성
```python
# articles/models.py

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  # 객체가 처음 생성될 때 한 번만 현재 시간을 자동으로 기록 <수정할 때는 값이 바뀌지 않음>
  created_at = models.DateTimeField(auto_now_add = True)
  # 객체가 저장될 때마다 현재 시간을 자동으로 기록 <수정될 때마다 갱신>
  updated_at = models.DateTimeField(auto_now = True)
```

- 이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본값 설정이 필요
- 1번은 현재 대화를 유지하면서 직접 기본값을 입력하는 방법
  ```bash
  $ python manage.py makemigrations
  ```
- 2번은 현재 대화에서 나간 후 models.py에 기본값 관련 설정을 하는 방법
  ![대화에서 나간 후 기본값 설정](./Django/default_setting_out.png)

- 추가하는 필드의 기본값을 입력해야 하는 상황
- 날짜 데이터이기 때문에 직접 입력하기보다 Django가 제안하는 기본 값을 사용하는 것을 권장
- 아무것도 입력하지 않고 enter를 누르면 Django가 제안하는 기본 값으로 설정됨
- migrations 과정 종료 후 2번째 migration 파일이 생성됨을 확인
- 이처럼 Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함(마치 `git commit`과 유사)

  ![Django는 설계도를 쌓아감](./Django/model_field_add_delete_X.png)

- migrate 후 테이블 필드 변화 확인
  - `$ python manage.py migrate`

#### model class에 변경사항(1)이 생겼다면, 반드시 새로운 설계도를 생성(2)하고, 이를 DB에 반영(3)해야 한다.
1. model class 변경
2. makemigraitons
3. migrate

### 모델 필드
#### Model Field
- DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의

#### CharField()
- 길이의 제한이 있는 문자열을 넣을 때 사용 (필드의 최대 길이를 결정하는 max_length는 필수 인자)

#### TextField()
- 글자의 수가 많을 때 사용

#### DateTimeField()
- 날짜와 시간을 넣을 때 사용

### Admin site
#### Automatic admin interface
- Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- > 데이터 확인 및 테스트 등을 진행하는 데 매우 유용

#### 1. admin 계정 생성
- email은 선택사항이기 때문에 입력하지 않고 진행 가능
- 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
- `$ python manage.py createsuperuser`

#### 2. DB에 생성된 admin 계정 확인
  ![DB에 생성된 admin 계정 확인](./Django/check_admin_id_in_DB.png)

#### 3. admin에 모델 클래스 등록
- admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
  ```python
  # articles/admin.py

  from django.contrib import admin
  from .models import Article

  admin.site.register(Article)
  ```

#### 4. admin site 로그인 후 등록된 모델 클래스 확인
  ![admin site 로그인 후 등록된 모델 클래스 확인](./Django/check_entered_model_class.png)

#### 5. 데이터 생성, 수정, 삭제 테스트
  ![데이터 생성, 수정, 삭제 테스트](./Django/data_create_alter_delete_test.png)

#### 6. 테이블 확인
  ![테이블 확인](./Django/check_table.png)

## 4. ORM
#### ORM (Object - Relational - Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

#### ORM의 역할
  - 사용하는 언어가 다르기 때문에 소통 불가
  - Django에 내장된 ORM이 중간에서 이를 해석

### QuerySet API
#### QuerySet API
  - ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화하는 데 사용하는 도구
    - > API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

#### QuerySet API 구문
`Article.objects.all()`
- Article : Model class
- objects : Manager
- all() : QuerySet API

#### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- "쿼리문을 작성한다."
  - > 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

#### QuerySet
- 데이터베이스에게서 전달받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

#### QuerySet API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것

### QuerySet API 실습
#### Postman 설치 및 안내

#### URL과 HTTP requests methods 설계
|             | GET | POST | PUT | DELETE |
|:-----------:|:----------:|:----:|:----:|:----:|
|  articles/  | 전체 글 조회 | 글 작성 |  |  |
| articles/1/ | 1번 글 조회 |  | 1번 글 수정 | 1번 글 삭제 |

#### 스켈레톤 프로젝트 안내
1. 가상 환경 생성, 활성화 및 패키지 설치
  - 외부 패키지 및 라이브러리는 `requirements.txt`에 작성되어 있음
    ```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    $ pip install -r requirements.txt
    ```
2. migrate 진행
    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

3. 프로젝트는 '주석을 해제'하며 진행

#### Skeleton code 살펴보기
- `config/urls.py` 확인
  ```python
  # config/urls.py

  urlpatterns = [
    path("admin/", admin.site.urls),
    # path('articles', include('articles.urls')),
  ]
  ```
  - > <span style='color:red'>QuerySet API 실습에는 articles app을 사용함</span>
  
- `articles/urls.py` 확인
  ```python
  # config/urls.py

  urlpatterns = [
    # path('new/', views.article_create), 
    # path('list/', views.article_list),
    # path('<int:pk>/', views.article_detail),
    # path('<int:pk>/edit/', views.article_update),
    # path('<int:pk>/delete/', views.article_delete),
  ]
  ```
  - > <span style='color:red'>QuerySet API 실습에는 articles app을 사용함</span>

  - Article Model 클래스 확인
    ```python
    # articles/models.py

    class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()

      def __str__(self):
        return self.title
    ```

### Create
#### 데이터 객체를 만드는(생성하는) 3가지 방법
1. 첫번째 방법
    ```python
    article = Article() # Article(class)로부터 article(instance) 생성 후 저장
    # print(type(article)) # <class 'articles.models.Article'>

    # 클라이언트가 요청에 담아 보낸 데이터를 인스턴스 변수에 할당
    article.title = request.data.get('title')
    article.content = request.data.get('content')

    article.save()  # save를 해야 데이터베이스에 저장이 된다.
    print('article.id:', article.id) # article.id : 1
    ```
2. p.67


## 5. Django Serializer
### 개요
#### Serialization (직렬화)
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

#### Serialization 예시
- 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

### Serializer Class
#### Serializer
  - Serialization을 진행하여 Serialized data를 반환해주는 클래스

#### MOdelSerializer
  - Django 모델과 연결된 Serializer 클래스
    - > 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 Serialization을 진행


> 주연아... 필기 너무 잘했다... 무슨일이야... 루팡해가야지 하하하하하
  와 그리고 소리 너무좋아!! 오빠가 탐내는 이유 파악 완료 하하하하하 계속 치게 되네 앞으로 많은 필기 부탁해 소리가 좋으니까 (그리고 주연이도 좋아 하하하하ㅏ)