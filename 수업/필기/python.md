# Data Types / Control of Flow / Functions
## 목차
- Python
- Data Types
  - Data Types
  - Numeric Types
  - Sequence Types
  - Non-Sequence Types
  - Other Types
  - 복사
  - Type Conversion
- Operator
  - 기본 연산자
  - 단축평가
  - 멤버십 연산자
  - 시퀀스형 연산자
- Control of Flow
  - 제어문
  - 조건문
  - 반복문
  - List Comprehension
- Functions
  - 함수
  - 매개변수와 인자
  - Packing & Unpacking
  - 내장 함수
  - 람다 표현식
- 참고

## Python
### Python을 배우는 이유
- 쉽고 간결한 문법
  - 읽기 쉽고 쓰기 쉬운 문법 -> 쉽게 배우고 활용 가능
- 파이썬 커뮤니티의 지원
- 광범위한 응용 분야
  - 웹 개발 ,데이터 분석, 인공지능, 머신러닝, 자동화 스크립트 등

### Python의 데이터 분석 활용
- 풍부한 라이브러리
  - pandas, numpy, matplotlib 등 데이터 분석에 최적화된 라이브러리 제공
- 데이터 처리 및 시각화
  - 대용량 데이터 처리와 시각화를 쉽게 가능
- 머신러닝 및 인공지능
  - scikit-learn, tensorflow, keras 등의 라이브러리를 통해 머신러닝과 딥러닝 모델을 구현할 수 있음

### 알고리즘 구현에 유리한 Python
- 직관적인 문법
- 강력한 표준 라이브러리
- 빠른 프로토타이핑

---
**별도의 필기 파일보단 py파일에 주석으로 필기**

## Data Types
### 데이터 타입 분류
- Numeric Types
  - int(정수), float(실수), complex(복소수)
- Text Sequence Type
  - str(문자열)
- Sequence Types
  - list, tuple, range
- Non-sequence Types
  - set, dict
- 기타
  - Boolean, None, Functions

### 타입과 메서드
#### 메서드(Method)
- 객체에 속한 함수
- 객체의 상태를 조작하거나 동작을 수행

#### 메서드 특징
- 클래스(class) 내부에 정의되는 함수
- 파이썬에서 '타입을 표현하는 방법'
- help 함수를 통해 str을 호출해보면 class라는 것을 확인 가능

## Numeric Types
- int : 정수 자료형
- float : 실수 자료형

## Sequence Types
- 여러 개의 값들을 순서대로 나열하여 저장하는 자료형
- str, list, tuple, range

### Sequence Types 특징
1. 순서(Sequence)
- 값들이 순서대로 저장(정렬X)
2. 인덱싱(indexing)
- 각 값에 고유한 인덱스(번호)를 가지고 있음
- 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정 가능
3. 슬라이싱(Slicing)
- 인덱스 범위를 조절해 부분적인 값을 추출 가능
4. 길이(Length)
- len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
5. 반복(Iteration)
- 반복문을 사용하여 저장된 값들을 반복적으로 처리 가능

## str
### str
- **문자들의 순서가 있는 변경 불가능한 시퀀스 자료형**
- 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐
- 작은따옴표(') or 큰따옴표(")로 감싸서 표현

### f-string
- 문자열에 f 또는 F 접두어를 부티고 표현식을 {expression}로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있음
```python
bugs = 'roaches'
counts = 13
area = 'living room'

# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')
```
### 문자열의 시퀀스 특징
```python
my_str = 'hello'
# 인덱싱
print(my_str[1]) # e

# 슬라이싱
print(my_str[2:4]) # ll

# 길이
print(len(my_str)) # 5
```
### Python의 index
![python의 index](../00_startcamp/이미지/python의%20index.png)

### 슬라이싱(Slicing)
- 시퀀스의 일부분을 선택하여 추출하는 작업
- 시작 인덱스와 끝ㄴ 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성

## str 메서드
### 문자열 조작 메서드(새 문자열 반환)
1. `s.replace(old, new[, count])` : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
2. `s.strip[chars]` : 공백이나 특정 문자를 제거
3. `s.split(sep=None, maxsplit=-1)` : 공백이나 특정 문자를 기준으로 분리
4. `'separator'.join(iterable)` : 구분자로 iterable의 문자열을 연결한 문자열 반환

## list
### list
- **여러 개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형**
- 0개 이상의 객체를 포함하여 데이터 목록을 저장
- 대괄호([])로 표기
- 데이터는 어떤 자료형도 저장 가능
```python
my_list_1 = []

my_list_2 = [1, 'a', 3, 'b', 5]

my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
```
## list 메서드
### 리스트 값 추가 및 삭제 메서드
1. `L.append(x)` : 리스트 마지막에 항목 x를 추가
2. `L.extend(m)` : Iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능)
3. `L.pop(i)` : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거

### 리스트 탐색 및 정렬 메서드
1. `L.reverse()` : 리스트의 순서를 역순으로 변경(정렬X)
2. `L.sort()` : 리스트를 정렬(매개변수 이용가능)

## Tuple [기억만 하기]
### tuple
- **여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형**
- 0개 이상의 객체를 포함하여 데이터 목록을 저장
- 소괄호(())로 표기
- 데이터는 어떤 자료형도 저장할 수 있음

### 튜플 사용 목적
- 튜플의 불변 특성을 사용한 여러 개의 값을 전달, 그룹화, 다중 할당 등
-> 개발자가 직접 사용하기보다 '파이썬 내부 동작'에서 주로 이용

## Range
### range
- 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

### range 표현
- range(시작 값, 끝 값, 증가 값)
- range(n) : 0부터 (n-1)까지의 숫자의 시퀀스
- range(n, m) : n부터 (m-1)까지의 숫자 시퀀스

### range 특징
- 증가 값 X -> 1씩 증가
- 증가 값 < 0 -> 감소 / 증가 값 > 0 -> 증가
- 증가 값 == 0 -> Error

## Non-Sequence Types
### dict(딕셔너리)
- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

### 딕셔너리 표현
- key : **변경 불가능한 자료형**만 사용 가능(str, int, float, tuple, range, ...)
- value : 모든 자료형 사용 가능
- 중괄호 ({})로 표기

### 딕셔너리 사용
- key를 통해 value에 접근
```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]

# 추가
my_dict['banana'] = 50
print(my_dict) # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
```
### dict 메서드
#### 딕셔너리 메서드
1. `D.get(k)` : 키(k)에 연결된 값을 반환(키가 없으면 None 반환)
2. `D.get(k, v)` :키(k)에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환
3. `D.keys()` : 딕셔너리 D의 키를 모은 객체를 반환
4. `D.values()` : 딕셔너리 D의 값을 모은 객체를 반환
5. `D.items()` : 딕셔너리 D의 키/쌍을 모은 객체를 반환
6. `D.pop(k)` : 딕셔너리 D에서 키(k)를 제거하고 연결됐던 값을 반환 (없으면 오류)
7. `D.pop(k, v)` : 딕셔너리 D에서 키(k)를 제거하고 연결됐던 값을 반환 (없으면 v를 반환)

## Set
### Set
- 순서와 중복이 없는 변경 가능한 자료형
- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호({})로 표기
- 비어있는 set은 `my_set_1 = set()`으로 표기

### set 메서드
1. `s.add(x)` : 세트(s)에 항목(x)를 추가, 이미 x가 있다면 변화X
2. `s.remove(x)` : 세트(s)에서 항목(x)를 제거, 항목 x가 없을 경우, Key error

## Other Types
### None
- 파이썬에서 '값이 없음'을 표현하는 자료형
```python
variable = None
print(variable) # None

# 함수의 return이 없는 경우 None을 반환
def func():
  print('aaa')

print(func()) # None
```

### Boolean
- 참(True)과 거짓(False)을 표현하는 자료형
- 비교/논리 연산의 평가 결과로 사용
- 주로 조건 / 반복문과 함께 사용


## Type Conversion
### 암시적 형변환(Implicit Type conversion)
- 파이썬이 자동으로 형변환하는 것
- Boolean과 Numeric Type에서만 가능

### 명시적 형변환(Explicit Type conversion)
- 개발자가 직접 형변환하는 것
- 암시적 형변환이 아닌 경우를 모두 포함
- str -> integer : 형식에 맞는 숫자만 가능

## Operator
### 기본 연산자
#### 산술 연산자


## 제어문
### 제어문(Control Statement)
- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드 실행
- 조건문
  - if, elif, else
- 반복문
  - for, while
- 반복문 제어
  - break, continue, pass

### 조건문
#### if / elif / else
- 파이썬 조건문에 사용되는 키워드

### 반복문
#### for
- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

#### 반복 가능한 객체(iterable)
- 반복문에서 순회할 수 있는 객체(시퀀스 객체뿐만 아니라 dict, set 등도 포함)

#### 인덱스로 리스트 순회
- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경
```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2

print(numbers) # [8, 12, 20, -16, 10]
```

#### while
- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
  == 조건식이 거짓(False)가 될 때까지 반복


#### 반복 제어

## List Comprehension
### List Comprehension
- 간결하고 효율적인 리스트 생성 방법
```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```
## 함수의 구조
### 파이썬 함수의 특징
- def 키워드를 사용하여 정의
- 일급 객체
  - 함수가 변수에 할당될 수 있음
  - 함수가 다른 함수의 인자로 전달될 수 있음
  - 함수가 다른 함수에 의해 반환될 수 있음
- 익명 함수로 사용 가능(람다 표현식)

## 매개변수와 인자
### 매개변수와 인자 간 구분
- 매개변수(parameter)
  - 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
- 인자(argument)
  - 함수를 호출할 때, 실제로 전달되는 값

```python
def add_numbers(x, y) # x와 y는 매개변수(parameter)
  result = x + y
  return result

a = 2
b = 3
sum_resulot = add_numbers(a, b) # a와 b는 인자(argument)
print(sum_result)
```
## 다양한 인자 종류
### 1. 위치 인자(Positional Arguments)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- 위치인자는 함수 호출 시 반드시 값을 전달해야 함
```python
def greet(name, age) :
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
```

### 2. 기본 인자 값(Default Argument Values)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
```python
def greet(name, age=30) :
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
```

### 3. 키워드 인자(Keyword Arguments)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요X, 인자의 이름을 명시하여 전달
- 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함
```python
def greet(name, age) :
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name = 'Dave', age = 35) # 안녕하세요, Dave님! 35살이시군요.
greet(age = 35, 'Dave') # positional argument follows keyword argument
```

### 4. 임의의 인자 목록(Arbitrary Argument Lists)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
```python
def calculate_sum(*args) :
  print(args)
  total = sum(args)
  print(f'합계: {total}')
"""
(1, 2, 3)
합계: 6
"""

calculate_sum(1, 2, 3)
```

### 5. 임의의 키워드 인자 목록(Arbitrary Keyword Argument Lists)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리

## Packing & Unpacking
### Packing (패킹)
- 여러 개의 값을 하나의 변수로 묶어서 담는 것
- 변수에 담긴 값들은 튜플(tuple) 형태로 묶임

### '*'을 활용한 패킹
### '**'을 활용한 패킹

### Unpacking (언패킹)
- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당

### '*'을 활용한 언패킹
### '**'을 활용한 언패킹

## 내장 함수
### 내장 함수(Built-in Function)
- 파이썬이 기본적으로 제공하는 함수 ( 별도의 import 없이 바로 사용 가능 )

### 유용한 내장 함수 map & zip
#### map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

#### zip(*iterables)
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

## 람다 표현식
### 람다 표현식(Lambda Expressions)
- 익명 함수를 만드는 데 사용되는 표현식
- 한 줄로 간단한 함수를 정의


---
**05-functions/99-global.py에 필기 있음**

---
os를 조작하는 방법
서브프로세스를 실행하는 방법

과목
종류
세트번호

범위 1~6까지 혹은 a, b, c
를 반복해서
  git clone 을 받도록 하는
  base_url = 'http~~//{subject}