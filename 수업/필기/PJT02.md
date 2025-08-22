# DB 설계를 활용한 REST API 설계
<details>
<summary> 목차 </summary>

1. DRF With MySQL
  - 데이터 전처리
  - MySQL 연동
  - Customize RegisterSerializer

2. fixtures
  - fixtures 활용

3. 02 PJT 소개
  - DB 설계를 활용한 REST API 설계

</details>

## 1. DRF With MySQL
### 1) 데이터 전처리
#### 스켈레톤 코드 확인
- todos/models.py
  - user와 1:N 관계
  ```python
  from django.db import models
  from django.conf import settings

  # Create your models here
  class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 150)
  ```

  - data/completed_todos.csv
    - todos data
    - user 정보와 복합 구성

#### 데이터 구성 변경
- todo 테이블에는 title field만 정의됨
  - user FK 정보는 유지

- 그 외 user 정보는 user.csv로 별도 추출
  - namee은 first_name과 last_name으로 구분하여 저장

- 데이터 분리 함수 작성
  ```python
  def read_and_split_csv(file_path):
    todos = []
    users = {}
    with open(file_path, mode = 'r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
        todo = {'id' : row['id'], 'title' : row['title'], 'user_id' : row['user_id']}
        user = {
          'id' : row['user_id'],
          'first_name' : row['user_name'].split()[0],
          'last_name' : row['user_name'].split()[-1],
          'username' : row['user_username'],
          'email' : row['user_email']
        }
        todos.append(todo)
        users[row['user_id']] = user
    return todos, list(users.values())
  ```
- csv 파일 저장 함수 작성
  ```python
  def write_csv(file_path, data, fieldnames):
    with open(file_path, mode = 'w', newline='', encoding='utf-8') as file:
      writer = csv.DictWriter(file, fieldnames = fieldnames)
      writer.writeheader()
      writer.writerows(data)
  ```

- todo.csv, user.csv 분리하여 저장
  - todo에는 user FK를 저장하기 위해 user_id
  - user에는 user_id를 id로 저장
    ```python
    todos_fieldnames = ['id', 'title', 'user_id']
    write_csv(todos_output_file_path, todos, todos_fieldnames)

    users_fieldnames = ['id', 'first_name', 'last_name', 'username', 'email']
    write_csv(users_output_file_path, users, users_fieldnames)
    ```

### 2) MySQL 연동
#### mysqlclient
- support MySQL for python

#### mysqlclient 설치 및 설정
- mysqlclient 설치
  ```bash
  $ pip install mysqlclient
  $ pip freeze > requirements.txt
  ```
- settings.py에서 기존 DATABASES 주석 처리
  ```python
  # DATABASES = {
  #      'default' : {
  #           'ENGINE' : 'django.db.backends.sqlites3',
  #           'NAME' : BASE_DIR / 'db.sqlites3',
  #       }
  # }
  ```
  