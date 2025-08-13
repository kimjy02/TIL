# Django Relationships

<details>
<summary>목차</summary>

1. Many to one relationships
  - 댓글 모델

2. 관계 모델 참조

3. DRF with N:1 Relation
  - 사전 준비
  - 댓글 CRUD

4. Many to many relationships
  - N:1의 한계
  - 중개 모델
  - ManyToManyField
  - 'through' argument

5. ManyToManyField

6. 좋아요 기능 구현
  - 모델 관계 설정
  - 기능 구현

</details>

## 1. Many to one relationships
### 개요
#### Many to one relationships [N:1 or 1:N]
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

#### Comment(N: 0 이상) - Article(1)
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.

#### 테이블 관계
| Comment              |         | Article    |
|:--------------------:|:-------:|:----------:|
|     id               |         |   id       |
|   content            |         |  title     |
| created_at           |         |  content   |      
| updated_at           |         | created_at |
| Article에 대한 외래 키 |         | updated_at |

### 댓글 모델
#### ForeignKey()
- N : 1 관계 설정 모델 필드

#### 댓글 모델 정의
- ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 <span style='color:red'>단수형</span>으로 작성하는 것을 권장
- 외래 키는 ForeignKey 클래슬르 작성하는 위치와 관계없이 테입르 필드 마지막에 생성됨
```python
# articles/models.py

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete = models.CASCADE)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_new_add=True)
  updated_at = models.DateTimeField(auto_new=True)
```

<!-- #### p.12
- on_delete : id로 받은 article 게시글이 삭제된다면 어떻게 해야 하는가?
  - CASCADE : 참조하고 있는 대상이 삭제되면 나도 같이 삭제
  - ... -->

#### ForeignKey(<span style='color:red'> to </span>, on_delete)
- 참조하는 모델 class 이름

#### ForeignKey( to , <span style='color:red'> on_delete </span>)
- 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정 (데이터 무결성)

#### on_delete의 'CASCADE'
- 부모 객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제

#### Migration 이후 댓글 테이블 확인
- 댓글 테이블의 article_id 필드 확인
- 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유
  - > '참조 대상 클래스 이름' + '_' + '클래스 이름'


## 2. 관계 모델 참조
### 역참조
#### 역참조
- N:1 관계에서 1에서 N을 참조하거나 조회하는 것 [ 1 → N ]
- <span style='color:red'> N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 기능이 필요 </span>

#### 역참조 사용 예시
- `article.comment_set.all()`
  - article : 모델 인스턴스
  - <span style='color:red'>comment_set : related manager(역참조 이름)</span>
  - all() : QuerySet API
  - > 특정 게시글에 작성된 댓글 전체를 조회하는 명령

#### related manager
- N:1 혹은 M:N 고나계에서 역참조 시에 사용하는 매니저
- > 'objects' 매니저를 통해 QuerySet API를 사용했던 것처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨

#### related manager 이름 규칙
- N:1 관계에서 생성되는 Related manager의 이름은 참조하는 <span style='color:red'> "모델명_set" </span> 이름 규칙으로 만들어짐
- 특정 댓글의 게시글 참조(Comment → Article)
  - `comment.article`
- 특정 게시글의 댓글 목록 참조(Article → Comment)
  - `article.comment_set.all()`

## 3. DRF with DRF with N:1 Relation
### 사전 준비
#### Comment 모델 정의
- Comment 클래스 정의 및 데이터베이스 초기화
```python
# articles/models.py

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
```
- Migrate 작업 진행
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

#### URL 및 HTTP request method 구성
| URL                    | GET          | POST      | PUT          | DELETE       |
|:----------------------:|:------------:|:---------:|:------------:|:------------:|
| `comments/`            | 댓글 목록 조회 |           |              |              |
| `comments/1/`          | 단일 댓글 조회 |           | 단일 댓글 수정 | 단일 댓글 삭제 |
| `articles/1/comments/` |              | 댓글 생성  |

### POST
#### POST
- 댓글 생성을 위한 CommentSerializer 정의
```python
# articles/serializers.py

from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
```

- 단일 댓글 생성을 위한 url 및 view 함수 작성
```python
# articles/urls.py

urlpatterns = [
  ...,
  path('<int:article_pk>/comments/', views.comment_create),
]
```
```python
# articles/views.py
@api_view(['POST'])
def comment_create(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```
- serializer 인스턴스의 `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가 데이터를 받을 수 있음
```python
# articles/views.py
@api_view(['POST'])
def comment_create(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(article=article)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```
- POST `http://127.0.0.1:8000/articles/{article_pk}/comments/` 응답 확인
- > 상태코드 400 응답 확인
- > CommentSerializer에서 외래 키에 해당하는 article 필드 또한 사용자로부터 입력받로고 설정되어 있기 때문에 서버 측에서는 누락되었다고 판단한 것
- > 유효성 검사 목록에서 제외 필요
- > article 필드를 <span style='color:red'> 읽기 전용 필드</span>로 설정하기

#### 읽기 전용 필드(read_only_fields)
- 데이터를 전송받은 시점에서 "<span style='color:red'> 유효성 검사에서 제외</span>시키고, <span style='color:red'> 데이터 조회 시에는 출력</span>"하는 필드
```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('article',)
```

### GET
#### GET - List
- url 작성
```python
urlpatterns = [
  ...,
  path('comments/', views.comment_list),
]
```
- view 함수 작성
```python