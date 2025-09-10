# SQL Advanced
<details>
<summary>Index</summary>

1. JOIN
    - JOIN clause
    - INNER JOIN/LEFT JOIN/RIGHT JOIN/SELF JOIN

2. Subquery
    - Single-row Subquery/Multi-row Subquery/Multi-column Subquery

3. Database Index
    - INDEX / INDEX 종류
    - INDEX 생성/추가하기 / INDEX 사용하기 / INDEX 삭제하기

4. 참고
    - VIEW / B-tree
</details>

## 1. JOIN
### 1) 개요
#### 관계
- <span style='color:red'>여러</span> 테이블 간의 (논리적) 연결

#### 관계의 필요성
- 커뮤니티 게시판에 필요한 데이터 생각해보기

  | id | title | content | writer |   role  |
  |:--:|:-----:|:-------:|:------:|:-------:|
  | 1  | 제목1 |  내용1  | 하석주 |  admin  |
  | 2  | 제목2 |  내용2  | 정윤미 | student |
  | 3  | 제목3 |  내용3  | 유하선 | student |

- '하석주'가 작성한 모든 게시글을 조회하기
-  어떤 문제점이 있을까?
   -  > 동명이인이 있다면 혹은 특정 데이터가 수정된다면?
      -  `SELECT * FROM 테이블 WHERE writer = '하석주';`
- 테이블을 나누어서 분류하자
- articles
    | id | title | content |
    |:--:|:-----:|:-------:|
    | 1 | 제목1 | 내용1 | 
    | 2 | 제목2 | 내용2 |
    | 3 | 제목3 | 내용3 |
- users
    | id | name |
    |:--:|:----:|
    | 1 | 하석주 |
    | 2 | 정윤미 |
    | 3 | 유하선 |
- roles
     | id | role |
    |:--:|:----:|
    | 1 | admin |
    | 2 | staff |
    | 3 | student |

    - > 각 게시글은 누가 작성했는지 알 수 있을까?
    - > 작성자들의 역할은 무엇일까?

- articles와 users 테이블에 각각 userId, roleId 외래 키 필드 작성
- articles
    | id | title | content | userId |
    |:--:|:-----:|:-------:|:------:|
    | 1 | 제목1 | 내용1 | 1 |
    | 2 | 제목2 | 내용2 | 1 |
    | 3 | 제목3 | 내용3 | 3 |
- users
    | id | name | roleId |
    |:--:|:----:|:------:|
    | 1 | 하석주 | 1 |
    | 2 | 정윤미 | 3 |
    | 3 | 유하선 | 2 |
- roles
     | id | role |
    |:--:|:----:|
    | 1 | admin |
    | 2 | staff |
    | 3 | student |

- 관리자인 사람만 보고 싶다면?
    - > roleId가 1인 데이터 조회
- 하석자라는 사람이 권미숙으로 개명한다면?
    - > users에서 한 번만 변경하면 자동으로 모두 변경

#### JOIN이 필요한 순간
- 테이블을 분리하면 데이터 관리는 용이해질 수 있으나 출력 시에는 문제가 있음
- 테이블 한 개만을 출력할 수 밖에 없어 **다른 테이블과 결합하여 출력**해야 함
- 이때 사용하는 것이 **'JOIN'** 

### 2) JOIN clause
#### <span style='color:red'>JOIN</span> clause
- 둘 이상의 테이블에서 데이터를 검색하는 방법

#### JOIN 종류
1. INNER JOIN
2. LEFT JOIN
3. RIGHT JOIN
4. SELF JOIN

#### 사전 준비
[코드실행](../08_db/03_SQL_Adv/07_Join.sql)

### 3) INNER JOIN
#### <span style='color:red'>INNER JOIN</span> clause
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

#### INNER JOIN syntax
```SQL
SELECT 
    select_list
FROM
    table_a
INNER JOIN table_b
    ON table_b.fk = table_a.pk;
```
- FROM 절 이후 메인 테이블 지정(table_a)
- INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정 (table_b)
- ON 키워드 이후 조인 조건을 작성
- 조인 조건은 table_a와 table_b 간의 레코드를 일치시키는 규칙을 지정

#### INNER JOIN 예시
- articles
    | id | title | content | userId |
    |:--:|:-----:|:-------:|:------:|
    | 1 | 제목1 | 내용1 | 1 |
    | 2 | 제목2 | 내용2 | 2 |
    | 3 | 제목3 | 내용3 | NULL |
    | 4 | 제목4 | 내용4 | 3 |
    | 5 | 제목5 | 내용5 | 1 |
    | 6 | 제목6 | 내용6 | NULL |
    | 7 | 제목7 | 내용7 | 5 |

- users
    | id | name | age | parent_id |
    |:--:|:----:|:---:|:---------:|
    | 1 | 하석주 | 50 | NULL |
    | 2 | 정윤미 | 48 | NULL |
    | 3 | 유하선 | 46 | NULL |
    | 4 | 하민성 | 24 | 1 |
    | 5 | 정아인 | 22 | 2 |
    | 6 | 송민 | 19 | 1 |
    | 7 | 정지민 | 22 | 2 |
- 작성자가 있는 (존재하는 회원) 모든 게시글을 작성자 정보와 함께 조회
  ```SQL
  SELECT articles.*, users.id, users.name FROM articles
  INNER JOIN users
    ON users.id = articles.userId;
  ```

#### INNER JOIN 활용 1
- 1번 회원(하석주)가 작성한 모든 게시글의 제목과 작성자명을 조회
    | title | name |
    |:-----:|:----:|
    | 제목1 | 하석주 |
    | 제목5 | 하석주 |

    ```sql
    SELECT articles.title, users.name
    FROM articles
    INNER JOIN users
        ON users,id = articles.userId
    WHERE users.id = 1;
    ```

### 4) LEFT JOIN
#### <span style='color:red'>LEFT JOIN</span> clause
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

#### LEFT JOIN syntax
```SQL
SELECT
    select_list
FROM
    table_a
LEFT JOIN table_b
    ON table_b.fk = table_a.pk;
```
- FROM 절 이후 왼쪽 테이블 지정(table_a)
- LEFT JOIN 절 이후 오른쪽 테이블 지정(table_a)
- ON 키워드 이후 조인 조건을 작성
  - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴

#### LEFT JOIN 예시
- articles
    | id | title | content | userId |
    |:--:|:-----:|:-------:|:------:|
    | 1 | 제목1 | 내용1 | 1 |
    | 2 | 제목2 | 내용2 | 2 |
    | 3 | 제목3 | 내용3 | NULL |
    | 4 | 제목4 | 내용4 | 3 |
    | 5 | 제목5 | 내용5 | 1 |
    | 6 | 제목6 | 내용6 | NULL |
    | 7 | 제목7 | 내용7 | 5 |

- users
    | id | name | age | parent_id |
    |:--:|:----:|:---:|:---------:|
    | 1 | 하석주 | 50 | NULL |
    | 2 | 정윤미 | 48 | NULL |
    | 3 | 유하선 | 46 | NULL |
    | 4 | 하민성 | 24 | 1 |
    | 5 | 정아인 | 22 | 2 |
    | 6 | 송민 | 19 | 1 |
    | 7 | 정지민 | 22 | 2 |
- 모든 게시글을 작성자 정보와 함께 조회

    | id | title | content | userId | id | name |
    |:--:|:-----:|:-------:|:------:|:--:|:----:|
    | 1 | 제목1 | 내용1 | 1 | 1 | 하석주 |
    | 2 | 제목2 | 내용2 | 2 | 2 | 정윤미 |
    | 3 | 제목3 | 내용3 | NULL | NULL | NULL |
    | 4 | 제목4 | 내용4 | 3 | 3 | 유하선 |
    | 5 | 제목5 | 내용5 | 1 | 1 | 하석주 |
    | 6 | 제목6 | 내용6 | NULL | NULL | NULL |
    | 7 | 제목7 | 내용7 | 5 | 5 | 정아인 |
    
    ```SQL
    SELECT articles.*, users.id, users.name FROM articles
    LEFT JOIN users
        ON users.id = articles.userId;
    ```

#### LEFT JOIN 특징
- 왼쪽 테이블의 모든 레코드를 표기
- 오른쪽 테이블과 매칭되는 레코드가 없으면 NULL을 표시

#### LEFT JOIN 활용 1
- 게시글을 작성한 이력이 없는 회원의 name 조회
    | name |
    |:----:|
    |하민성|
    | 송민 |
    |정지민|

- users
    | id | name | age | parent_id |
    |:--:|:----:|:---:|:---------:|
    | 1 | 하석주 | 50 | NULL |
    | 2 | 정윤미 | 48 | NULL |
    | 3 | 유하선 | 46 | NULL |
    | 4 | 하민성 | 24 | 1 |
    | 5 | 정아인 | 22 | 2 |
    | 6 | 송민 | 19 | 1 |
    | 7 | 정지민 | 22 | 2 |

- articles
    | id | title | content | userId |
    |:--:|:-----:|:-------:|:------:|
    | 1 | 제목1 | 내용1 | 1 |
    | 2 | 제목2 | 내용2 | 2 |
    | 3 | 제목3 | 내용3 | NULL |
    | 4 | 제목4 | 내용4 | 3 |
    | 5 | 제목5 | 내용5 | 1 |
    | 6 | 제목6 | 내용6 | NULL |
    | 7 | 제목7 | 내용7 | 5 |

- 최종
  | id | name | id | title | content | userId |
  |:--:|:----:|:--:|:-----:|:-------:|:------:|
  | 1 | 하석주 | 1 | 제목1 | 내용1 | 1 |
  | 1 | 하석주 | 5 | 제목5 | 내용5 | 1 |
  | 2 | 정윤미 | 2 | 제목2 | 내용2 | 2 |
  | 3 | 유하선 | 4 | 제목4 | 내용4 | 3 |
  | 4 | 하민성 | NULL | NULL | NULL | NULL |
  | 5 | 정아인 | 7 | 제목7 | 내용7 | 5 |
  | 6 | 송민 | NULL | NULL | NULL | NULL |
  | 7 | 정지민 | NULL | NULL | NULL | NULL |

  ```SQL
  SELECT users.name
  FROM users
  LEFT JOIN articles
    ON articles.userId = users.id
  WHERE articles.userId IS NULL;
  ```

### 5) RIGHT JOIN
#### RIGHT JOIN syntax
```SQL
SELECT
    select_list
FROM
    table_a
RIGHT JOIN table_b
    ON table_b.fk = table_a.pk;
```
- FROM 절 이후 왼쪽 테이블 지정(table_a)
- LEFT JOIN 절 이후 오른쪽 테이블 지정(table_b)
- ON 키워드 이후 조인 조건을 작성
  - 오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴

### 6) SELF JOIN
#### SELF JOIN clause
- 동일한 테이블의 컬럼을 비교하여 일치하는 데이터를 추가로 붙여 반환
- 주로 계층적 데이터 구조를 표현하거나 동일 테이블 내에서 특정 관계를 찾을 때 사용

#### SELF JOIN syntax
```SQL
SELECT
    select_list
FROM
    table_a
[INNER] JOIN table_a t_a
    ON table_a.column = t_a.column;
```
- FROM 절 이후 본 테이블 지정(table_a)
- JOIN 절 이후 본 테이블 지정(table_a)
  - 이때 반드시 별칭 설정
- ON 키워드 이후 조인 조건을 작성
  - 본 테이블의 컬럼과 별칭 테이블의 컬럼을 이용하여 비교
