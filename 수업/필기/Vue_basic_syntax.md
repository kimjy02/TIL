# Basic Syntax
<details>
<summary>Index</summary>

1. Template Syntax

2. Dynamically data binding
   - v-bind

3. Event Handling
   - v-on

4. Form Input Bindings
   - v-model

5. Conditional Rendering
    - v-if
    - v-if vs. v-show

6. List Rendering
    - v-for
</details>

## 1. Template Syntax
### 1) 개요
#### Template Syntax
- DOM을 기본 구성 요소 인스턴스의 데이테에 <span style='color:red'>선언적으로 바인딩(Vue Instance와 DOM을 연결)</span>할 수 있는 HTML 기반 <span style='color:red'>템플릿 구문(확장된 문법 제공)</span>을 사용

#### Template Syntax 종류
1. Text Interpolation
2. Raw HTML
3. Attribute Bindings
4. JavaScript Expressions

#### 1. Text Interpolation
    `<p>Message: {{ msg }}</p>`
 - 데이터 바인딩의 가장 기본적인 형태
 - 이중 중괄호 구문(콧수염 구문)을 사용
 - 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
 - msg 속성이 변경될 때마다 업데이트 됨

#### 2. Raw HTML
    <div v-html='rawHtml'></div>
    const rawHtml = ref('<span style="color:red"> This should be red.</span>')
- 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

#### 3. Attribute Bindings
    <div v-bind:id="dynamicId"></div>
    const dynamicId = ref('my-id')
    <div id='my-id'></div>
- 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
- HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
- 바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨

#### 4. JavaScript Expressions
    {{ number + 1 }}
    {{ ok ? 'YES' : 'NO' }}
    {{ message.split('').reverse().join('') }}
    <div : id = "`list-${id}`"></div>
- Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
- Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
    1. 콧수염 구문 내부
    2. 모든 directive의 속성 값("v-"로 시작하는 특수 속성)

#### Expressions 주의사항
- 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
  - 표현식은 값으로 평가할 수 있는 코드 조각 (return 뒤에 사용할 수 있는 코드여야 함)
- 작동하지 않는 경우
  ```html
  <!-- 표현식이 아닌 선언식 -->
  {{ const number = 1 }}

  <!-- 제어문은 삼항 표현식을 사용해야 함 -->
  {{ if (ok) { return message } }}
  ```

### 2) Directive
#### Directive
- 'v-' 접두사가 있는 특수 속성

#### Directive 특징
- Directive의 속성 값은 단일 JavaScript 표현식이여야 함(v-fore, v-on 제외)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용

- 예시
    `<p v-if = 'seen'>Hi There</p>`

unpacking해서 쓰고 싶을 때, item이 먼저 나오고 index가 나옴