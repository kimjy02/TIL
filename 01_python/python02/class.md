# Classes
## 목차
1. 객체
2. 클래스
3. 메서드
4. 상속
5. 클래스 참고
  - 메서드 주의사항
  - 매직메서드
  - 데코레이터
6. 참고
  - 제네레이터
  - 에러와 예외
  - 모듈
  - 파일 입출력
  - 정규표현식

## 객체
### 객체
#### 클래스(Class)
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공

#### 객체(Object)
- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- **속성**과 **행동**으로 구성된 모든 것

#### 객체 예시
![객체 예시(1/2)](../../00_startcamp/이미지/객체%20예시1.png)
![객체 예시(2/2)](../../00_startcamp/이미지/객체%20예시2.png)

#### 클래스와 객체
- 인스턴스 : 클래스로 만든 객체
  - 가수(클래스)
    -> 아이유는 객체다 (O)
    -> 아이유는 인스턴스다 (△)
    -> 아이유는 가수의 인스턴스다 (O)

- [클래스(가수)]와 객체(아이유)
  -> 타입(list) : 클래스를 만든다 == **타입**을 만든다

- 변수 name의 타입 : str 클래스
- 변수 name : str 클래스의 인스턴스
```python
name = 'Alice'
print(type(name)) # <class 'str>
```
#### 메서드 [객체.행동()/ 인스턴스.메서드()]
- `"hello".upper()` : 문자열.대문자로
- `[1,2,3].sort()` : 리스트.정렬해()

**하나의 객체(object) : 특정 타입의 인스턴스(instance)**
  - 123, 900, 5 : 모두 int의 인스턴스
  - 'hello', 'bye' : 모두 string의 인스턴스
  - [232, 89, 1], [] : 모두 list의 인스턴스

#### 객체 정리
- 타입(Type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
- 객체(Object) = 속성(Attribute) + 기능(Method)

## 클래스
### 클래스
#### 클래스(Class)
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한  설계도
- 데이터와 기능을 함께 묶는 방법을 제공

#### 클래스 정의
- class 키워드
- 클래스 이름 : 파스칼 케이스(Pascal Case : 앞글자 대문자) 방식으로 작성
```python
class MyClass:
  pass
```
#### 인스턴스 생성 및 활용
```python
# 클래스 정의
class Person:
  blood_color = 'red'
  def __init__(self, name):
    self.name = name
  def singing(self):
    return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing()) # iu가 노래합니다.
# 속성(변수) 접근
print(singer1.blood_color) #red
```
### 클래스 구성요소
#### 생성자 함수
- 객체를 생성할 때 자동으로 호출되는 특별한 메서드
- __init__메서드로 정의되며, 객체 초기화를 담당
- 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
![생성자 함수](../../00_startcamp/이미지/생성자%20함수.png)

#### 인스턴스 변수
- 인스턴스마다 별도로 유지되는 변수
- 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
![인스턴스 변수](../../00_startcamp/이미지/인스턴스%20변수.png)

#### 클래스 변수
- 클래스 내부에 선언된 변수
- 클래스로 생성된 모든 인스턴스들이 공유하는 변수
![클래스 변수](../../00_startcamp/이미지/클래스%20변수.png)

#### 인스턴스 메서드
- 각 인스턴스에서 호출할 수 있는 메서드
- 인스턴스 변수에 접근하고 수정하는 등의 작업 수행
![인스턴스 메서드](../../00_startcamp/이미지/인스턴스%20메서드.png)

### 인스턴스 변수와 클래스 변수
#### 클래스 변수 활용
- 가수가 몇 명인지 확인하고 싶다면?
  - 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정할 수 있음
```python
class Person:
  count = 0
  
  def __init__(self, name):
    self.name = name
    Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')
print(Person.count) # 2
```

#### 클래스 변수와 인스턴스 변수
- **class.class_variable**로 클래스 변수 참조
```python
class Circle:
  pi = 3.14

  def __init__(self, r):
    self.r = r

c1 = Circle(5)
c2 = Circle(10)
```

## 메서드
### 메서드
#### 메서드 종류
1. 인스턴스 메서드
2. 클래스 메서드
3. 정적 메서드

### 인스턴스 메서드
#### 인스턴스 메서드
- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
  - 인스턴스의 상태를 조작하거나 동작을 수행
- 반드시 첫 번째 매개변수로 **인스턴스 자신(self)**을 전달받음
```python
class MyClass:

  def instance_method(self, arg1, ...):
    pass
  # self는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능
  # but 다른 이름을 사용하지 않을 것을 강력히 권장
```

#### self 동작 원리
- upper 메서드를 사용해 문자열 'hello'를 대문자로 변경하기
  ```python
  'hello'.upper()
  # 하지만 실제 파이썬 내부 동작은 다음과 같이 진행
  str.upper('hello')
  ```
- str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것
- 인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유
- `'hello'.upper()`은 `str.upper('hello')`를 객체 지향 방식의 메서드로 호출하는 표현(단축형 호출)
- 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현


#### 생성자 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값 설정
```python
class Person:
  def __init__(self, name):
    self.name = name
    print('인스턴스가 생성되었습니다.')
  
  def greeting(self):
    print(f'안녕하세요. {self.name}입니다.')

person1 = Person('지민') # 인스턴스가 생성되었습니다.
person1.greeting() # 안녕하세요. 지민입니다.
```

### 클래스 메서드
#### 클래스 메서드
- 클래스가 호출하는 메서드
  - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
```python
class MyClass:

    @classmethod
    def class_method(cls, arg1, ...):
      pass
    # cls는 매개변수 이름일 뿐, 다름 이름으로 설정 가능
    # but 다른 이름을 사용하지 않을 것을 권장
```
#### 클래스 메서드 예시
- 인자 cls는 Person 클래스가 전달됨
```python
class Person:
  count = 0

  def __init__(self, name):
    self.name = name
    Person.count += 1

  @classmethod
  def nnumber_of_population(cls):
    print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person("BTS")

# 인구수는 2입니다.
Person.number_of_populuation()
```

### 정적 메서드
#### 정적 메서드
- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
  - 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
- @staticmethod 데코레이터를 사용하여 정의
- 호출 시 필수적으로 작성해야 할 매개변수 X
```python
class MyClass:

  @staticmethod
  def static_method(arg1, ...):
    pass
```

#### 정적 메서드 예시
- 단순히 문자열을 조작하는 기능을 제공하는 정적 메서드
```python
class StringUtils:
  @staticmethod
  def reverse_string(string):
    return string[::-1]
  
  @staticmethod
  def capitalize_string(string):
    return string.capitalize()

text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text) # dlrow, olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_Text) # Hello, world
```

### 인스턴스와 클래스 간 이름 공간
#### 인스턴스와 클래스 간의 이름 공간
- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색
![인스턴스와 클래스 간의 이름 공간](../../00_startcamp/이미지/인스턴스와%20클래스%20간의%20이름%20공간.png)

## 상속
### 클래스 상속
#### 상속 없이 구현하는 경우
- 학생 / 교수 정보를 별도로 표현하기 어려움
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk() # 반갑습니다. 박교수입니다.
```

- 교수 / 학생 클래스로 분리했지만 메서드가 중복으로 정의될 수 있음
```python
class Professor:
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department

  def talk(self): # 중복
    print(f'반갑습니다. {self.name}입니다.')

class Student:
  def __init__(self, name, age, gpa):
    self.name = name
    self.age = age
    self.gpa = gpa
  
  def talk(self): # 중복
    print(f'반갑습니다. {self.name}입니다.')
```
#### 상속을 사용한 계층구조 변경
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def talk(self): # 메서드 재사용
    print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department

class Student(Person):
  def __init__(self, name, age, gpa):
    self.name = name
    self.age = age
    self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```

### 다중 상속
#### 다중 상속
- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

#### 다중 상속 예시
```python
class Person:
  def __init__(self, name):
    self.name = name
  
  def greeting(self):
    return f'안녕, {self.name}'

class Mom(Person):
  gene = 'XX'

  def swim(self):
    return '엄마가 수영'

class Dad(Person):
  gene = 'XY'

  def walk(self):
    return '아빠가 걷기'

class FirstChild(Dad, Mom):
  def swim(self):
    return '첫째가 수영'
  
  def cry(self):
    return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY
```

#### 다이아몬드 문제(The diamond problem)
- 두 클래스 B와 C가 A에서 상속되고 클래스 D와 B와 C 모두에서 상속될 때 발생하는 모호함
- B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의하지 않은 경우라면
- D는 B의 메서드 중 어떤 버전을 상속하는가? 아니면 C의 메서드 버전을 상속하는가?

#### 파이썬에서의 해결책
- MRO(Method Resolution Order) 알고리즘을 사용해 클래스 목록 생성
- 부모 클래스로부터 상속된 속성들의 검색을 C3 선형화 규칙에 맞춰 진행
- 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
- 속성이 D에서 발견되지 않으면 B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾는 순으로 진행됨

#### `super()`
- 부모 클래스(또는 상위 클래스)의 메서드를 호출하기 위해 사용하는 내장 함수
- 다중 상속 시 MRO(메서드 결정 순서)를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

#### `super()` 사용 에시 (단일 상속)
```python
# 사용 전
class Person:
  def __init__(self, name, age, number, email):
    self.name = name
    self.age = age
    self.number = number
    self.email = email

class Student(Person):
  def __init__(self, name, age, number, email, student_id):
    self.name = name
    self.age = age
    self.number = number
    self.email = email
    self.student_id = student_id

# 사용 후
class Person:
  def __init__(self, name, age, number, email):
    self.name = name
    self.age = age
    self.number = number
    self.email = email

class Student(Person):
  def __init__(self, name, age, number,  email, student_id):
    # Person의 init 메서드 호출
    super().__init__(name, age, number, email)
    self.student_id = student_id
```
#### `super()` 사용 예시 (다중 상속)
```python
# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')
```

#### MRO가 필요한 이유

## 클래스 참고
### 메서드 주의사항

### 매직 메서드
#### 매직 메서드(magic method)
- 인스턴스 메서드
- 특정 상황에 자동으로 호출되는 메서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
- 스페셜 메서드 혹은 매직 메서드라고 불림
- 예시
  - `__str__(self)`, `__len__(self)`, ...

#### 매직 메서드 예시
- `__str__(self)`
  - 내장 함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

### 데코레이터
#### 데코레이터(Decorator)
- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

## 참고
## 제너레이터
### 이터레이터
#### 이터레이터(Iterator)
- 반복 가능한 객체의 요소를 하나씩 반환하는 객체

#### Python 내부적으로 반복이 동작하는 원리
1. 내부적으로 for 문이 동작할 때 반복가능한 객체에 대해 iter()를 호출
2. iter() 함수는 메서드 `__next__()`를 정의하는 이터레이터 객체를 돌려줌
3. `__next__()` 메서드는 반복 가능한 객체들의 요소들을 한 번에 하나씩 접근
4. 남은 요소가 없으면 StopIteration 예외를 일으켜서 for 반복 종료를 알림

### 제너레이터
#### 제너레이터(Generator)
- 이터레이터를 간단하게 만드는 함수

#### 제너레이터를 사용하는 이유
1. 메모리 효율성
  - **한 번에 한 개의 값만 생성** : 제너레이터는 값을 하나씩 생성하여 반환하므로, 전체 시퀀스를 한 번에 메모리에 로드하지 않아도 됨
  - **대용량 데이터 처리** : 대용량 데이터셋을 처리할 때 메모리 사용을 최소화할 수 있음
    - 예 : 파일의 각 줄을 한 번에 하나씩 읽어 처리 가능
2. 무한 시퀀스 처리
  - **무한 시퀀스 생성**
    - 무한 루프를 통해 무한 시퀀스를 생성할 수 있음
    - 이는 끝이 없는 데이터 스트림을 처리할 때 유용
3. 지연 평가(Lazy Evaluation)
  - **필요할 때만 값 생성**
    - 제너레이터는 값이 실제로 필요할 때만 값을 생성
    - 이를 통해 불필요한 계산을 피하고 성능을 최적화할 수 있음
  - **연산 지연** : 복잡한 연산을 지연하여 수행할 수 있어 계산이 필요한 시점에만 연산이 이루어짐

#### 제너레이터 구조
- 일반적인 함수처럼 작성
- yield문을 사용하여 값 반환

#### 제너레이터 특징
- 클래스 기반의 이터레이터를 만들 필요 없이 `__iter__(), __next__()` 메서드가 저절로 만들어짐
- self.index나 self.data와 같은 인스턴스 변수를 사용하는 접근법에 비교해 함수를 쓰기 쉽고 명료하게 만듦

#### 제너레이터 구조 예시
- 제너레이터 통해 반복가능한 객체를 생성하고 호출하면 다음 순서를 기억함
- 호출하기 전에는 모든 값을 메모리에 올리지 않음
  - 지연 평가(Lazy Evaluation)
- 제너레이터로 반복 가능한 객체를 만들지 않으면 선언과 동시에 메모리 소모

#### return과 yield 차이
- return
  - 값을 반환하고 함수 실행을 종료
  - 함수 호출 시마다 전체 함수가 실행
  - 함수 상태는 호출 후 유지되지 않음

- yield
  - 값을 반환하지만 함수 실행을 종료하지 않음
  - 함수의 현재 상태를 유지하여, 이후 호출 시 중단된 지점부터 실행됨
  - 제너레이터 객체를 반환하며, 반복문을 통해 순차적으로 값을 반환 가능

### 제너레이터 활용



### 정규표현식
#### 정규표현식
- 문자열에서 특정 패턴을 찾기 위해 사용되는 기법
- 복잡한 문자열 속에서 특정한 규칙으로 된 문자열을 검색, 치환, 추출 등을 간결하게 수행할 수 있음

**EOL & EOF** X