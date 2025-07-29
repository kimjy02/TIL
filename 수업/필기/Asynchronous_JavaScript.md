# Asynchronous JavaScript
<details>
<summary> 목차 </summary>

1. 객체
- 구조 및 속성
- 객체와 함수
- this
- 추가 객체 문법

2. 배열
- 배열 메서드
- Array helper method
- 추가 배열 문법

3. 비동기

4. AJAX
- XHR

5. Callback과 Promise

6. Axios
</details>

## 객체
### 개요
#### Object
- 키로 구분된 데이터 집합(data collection)을 저장하는 자료형

### 구조 및 속성
#### 객체 구조
- 중괄호('{}')를 이용해 작성
- 중괄호 안에는 `key: value`쌍으로 구성된 속성(property)를 여러 개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용
```javascript
const user = {
  name: 'Alice',
  'key with space': true,
  greeting: function () {
    return 'hello'
  }
}
```
#### 속성 참조
- 점('.', chainging operator) 또는 대괄호('[]')로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
```javascript
// 조회
console.log(user.name) // Alice
console.log(user['key with space']) // true

// 추가
user.address = 'Korea'
console.log(user) // {name: 'Alice', key with space: true, address: 'Korea', greeting: f}

// 수정
user.name = "Bella"
console.log(user.name) // Bella

// 삭제
delete user.name
console.log(user) // {key with space: true, address: 'Korea', greeting: f}
```

#### 'in' 연산자
- 속성이 객체에 존재하는지 여부를 확인
```javascript
console.log('greeting' in user) // true
console.log('country' in user) // false
```

### 객체와 함수
#### Method
- 객체 속성에 정의된 함수
- `object.method()` 방식으로 호출
- 메서드는 객체를 '행동'할 수 있게 함
```javascript
console.log(user.greeting()) // hello
```

### this
#### Method
- 객체 속성에 정의된 함수
- <span style='color:red'>'this'</span> 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음

#### 'this' **keyword**
- 함수나 메서드를 호출한 객체를 가리키는 키워드
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

#### Method & this 사용 예시
```javascript
const person = {
  name: 'Alice',
  greeting: function () {
    return `Hello my name is ${this.name}`
  },
}
console.log(person.greeting()) // Hello my name is Alice
```

#### JavaScript에서 this는 함수를 <span style='color:red'>"호출하는 방법"</span>에 따라 가리키는 대상이 다름
- 단순 호출 : 전역 객체
- 메서드 호출 : 메서드를 호출한 객체

#### 1. 단순 호출 시 this
- 가리키는 대상 => 전역 객체
```javascript
const myFunc = function () {
  return this
}
console.log(myFunc()) // window
```

#### 2. 메서드 호출 시 this
- 가리키는 대상 => 메서드를 호출한 객체
``` javascript
const myObj = {
  data: 1,
  myFunc: function () {
    return this
  }
}
console.log(myObj.myFunc()) // myObj
```
#### 중첩된 함수에서의 this 문제점과 해결책
- forEach의 인자로 작성된 함수는 일반적인 함수 호출이기 떄문에 this가 전역 객체를 가리킴
```javascript
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this) // window
    })
  }
}
console.log(myObj2.myFunc())
```
= >
- <span style='color:red'>화살표 함수는 자신만의 this를 가지지 않기 때문에</span> 외부 함수(myFunc)에서의 this 값을 가져옴
```javascript
const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this) // myObj3
    })
  }
}
console.log(myObj3.myFunc())
```

#### JavaScript 'this' 정리
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달받음
- JavaScript에서 this는 함수가 '호출되는 방식'에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해 JavaScript의 this는 <span style='color:red'>함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정</span>됨(동적 할당)
- this가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은
- 장점 : 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
- 단점 : 이런 유연함이 실수로 이어질 수 있다는 것
- > 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데 집중

### 추가 객체 문법
#### 1. 단축 속성
- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음
```javascript
const name = 'Alice'
const age = 30

const user = {
  name: name,
  age: age,
}
// =>
const user = {
  name,
  age,
}
```

#### 2. 단축 메서드
- 메서드 선언 시 function 키워드 생략 가능
```javascript
const myObj1 = {
  myFunc: function() {
    return 'Hello'
  }
}
// =>
const myObj2 = {
  myFunc() {
    return 'Hello'
  }
}
```
#### 3. 계산된 속성(computed property name)
- 키가 대괄호([])로 둘러싸여 있는 속성
- > 고정된 값이 아닌 변수 값을 사용할 수 있음
```javascript
const product = prompt('물건 이름을 입력해주세요.')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix + suffix]: 'value',
}
console.log(bag) // {연필: 5, myproperty: 'value'}
```

#### 4. 구조 분해 할당(destructing assignment)
- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법
```javascript
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}
const firstName = userInfo.name
const userId = userInfo.userId
const email = userInfo.email
// =>
const { firstName } = userInfo
const { firstName, userId } = userInfo
const { firstName, userId, email }= userInfo

console.log(firstName, userId, email)
// Alice alice123 alice123@gmail.com
```
- '함수의 매개변수'로 객체 구조 분해 할당 활용 가능
```javascript
const person = {
  name: 'Bob',
  age: 35,
  city: 'London',
}

function printInfo({ name, age, city }) {
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}
// 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
printInfo(person) // 이름: Bob, 나이: 35, 도시: London
```

#### 5. Object with '전개 구문'
- "객체 복사"
  - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능
```javascript
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

#### 6. 유용한 객체 메서드
- `Object.keys()`
- `Object.values()`
```javascript
const profile = {
  name: 'Alice',
  age: 30,
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.values(profile)) // ['Alice', 30]
```

#### 7. Optional chaining('?.')

### new 참고 시험 안 나옴
