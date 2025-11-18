# 데이터엔지니어링 기초 - Spark RDD
<details>
<summary> 목차 </summary>

1. RDD의 개념과 특징 이해
2. RDD 생성 및 변환 학습

</details>

## 1. RDD의 개념과 특징 이해
### 1) RDD린?
#### RDD란?
- 대용량 데이터를 분산 처리하고 분석하기 위한 Spark의 기본 데이터 처리 단위
- Resilient(탄력적인)
- Distributed(분산된)
- Dataset(데이터셋)
  ![alt text](image.png)

### 2) RDD의 특징
#### (1) 데이터의 추상화(Data Abstraction)
![alt text](image-1.png)

#### (2) 탄력성(Resilient) & 불변성(Immutable)
- RDD는 한 번 생성되면 변경할 수 없음
- 어떤 노드(서버)가 장애로 인해 중단되더라도, 데이터 복구 가능
  ![alt text](image-2.png)

#### (3) 타입의 안정성 보장
- 어떠한 하나의 타입의 객체를 가질 수 있음
- 데이터 타입을 컴파일 시전에 검사
- 성능 최적화
- 코드의 가독성과 유지보수성 향상
- Pyspark를 쓸 때는 Python이 동적 타입 언어이기 때문에 타입 안정성이 적용되지는 않음

#### (4) 정형(Structured) & 비정형(Unstructured) 데이터
- 비정형 데이터 : 고정된 포맷이 없는 텍스트 데이터
  - > `sc.textFile()`을 활용해 RDD로 로딩 후, `map`, `filter`, `flatMap` 등으로 가공
- 정형 데이터 : 컬럼이 있는 테이블 형태 데이터
  - > DataFrame 또는 `RDD.map()`으로 가공

#### (5) 지연 평가(Lazy Evaluation)
- 중간 연산을 줄여 성능 최적화
- 실행 계획을 최적화하여 성능 향상
- 불필요한 연산 방지로 리소스 절약
  ![alt text](image-3.png)

### 3) Spark RDD란?
#### 주요 구성 요소 정리 코드
![alt text](image-4.png)

## 2. RDD 생성 및 변환 학습
### 1) Rdd 생성
#### (1) 기존의 메모리 데이터를 RDD로 변환하는 방법
- Python의 리스트(List)나 Scala의 컬렉션(Collection)을 RDD로 변환 가능
- 이 방법은 주로 테스트나 작은 데이터 셋을 다룰 때 사용

#### (2) 외부파일(텍스트, CSV, JSON 등)에서 RDD를 생성하는 방법
- 실무에서는 보통 파일이나 데이터베이스에서 데이터를 불러와야 함
- `sc.textFile("파일 경로")`, `spear.read.format('jdbc').option(...)`형태를 사용하여 외부 데이터로 RDD로 변환할 수 있음
