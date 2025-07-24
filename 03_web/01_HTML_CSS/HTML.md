# HTML & CSS
## 목차
1. 웹

2. 웹 구조화
  - HTML
  - Structure of HTML
  - Text Structure

3. 웹 스타일링
  - CSS
  - CSS 선택자
  - **명시도**

4. CSS Box Model
  - 박스 타입

5. 참고
  - 명시도 관련
  - HTML 스타일 가이드
  - CSS 스타일 가이드
  - MDN

## 웹
### 개요
#### World Wide Web
- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

#### Web
- Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

#### Web site
- 인터넷에서 여러 개의 Web page가 모인것
- 사용자들에게 정보나 서비스를 제공하는 공간

#### Web page
- HTML, CSS 등의 웹 기술을 이용하여 만들어진, "Web site"를 구성하는 하나의 요소
![Web page 구성 요소(1/2)](../00_startcamp/이미지/Web%20page%20구성요소.png)
![Web page 구성 요소(2/2)](../00_startcamp/이미지/Web%20page%20구성요소2.png)

## 웹 구조화
### HTML
#### HTML
- HyperText Markup Language
- 웹 페이지의 의미와 구조를 정의하는 언어

#### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

#### Hypertext 특징
- 비선형성
- 상호연결성
- 사용자 주도적 탐색
  ![Hypertext 특징](../00_startcamp/이미지/hypertext%20특징.png)

#### Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 예 : HTML, Markdown
  ![Markup Language](../00_startcamp/이미지/markup%20language.png)

#### Markup Language 예시
- ```HTML
  <h1>HTML</h1>
  <p> HTML이란 Hyper Text Markup Language의 약자이다. </p>
  <h2> Hyper Text </h2>
  <p> Hyper Text란 기존의 선형적인 텍스트가 아닌 비선형적으로 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다. 기본적으로 Hpyer Link를 통해 텍스트를 이동한다. </p>
  <p> 이러한 Hyper Text는 인간이 기억하는 방식까지 바꾸고 있는데 이를 컬럼비아대 벳시 스패로 교수팀은 구글 효과(Google Effect)라고 이름 붙이고, 해당 연구를 '사이언스'지에 게재하였다. </p>
  <h2> 구글 효과(Google Effect) </h2>
  <p> 구글 효과란 ... </p>
  ```

### Structure of HTML
#### HTML 구조
- `<!DOCTYPE html>`
  - 해당 문서가 html로 문서라는 것을 나타냄
- `<html></html>`
  - 전체 페이지의 콘텐츠를 포함
- `<title></title>`
  - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- `<head></head>`
  - HTML 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터를 작성
  - 사용자에게 보이지 않음
- `<body></body>`
  - HTML 문서의 내용을 나타냄
  - 페이지에 표시되는 모든 콘텐츠를 작성
  - 한 문서에 하나의 body 요소만 존재
  ```HTML
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
  </html>
  ```

#### HTML Element(요소)
  - 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
  - 닫는 태그는 태그 이름 앞에 슬래시가 포함됨
    - 닫는 태그가 없는 태그도 존재
      - 내용 구성을 어떻게 하느냐에 따라 달라짐
  - ![HTML Element](../00_startcamp/이미지/HTML%20Element.png)

#### HTML Attributes(속성)
- 사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값
- 목적
  - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용됨
-   - ![HTML Attribute](../00_startcamp/이미지/HTML%20Attribute.png)

#### HTML Attributes(속성) 작성 규칙
1. 속성은 요소 이름과 속성 사이에 공백이 있어야 함
2. 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
3. 속성 값은 열고 닫는 따옴표로 감싸야 함

---
- VSCode에서 html파일에서 ! + Tab : html 틀 생성
- alt + b : 실행
---

#### HTML 구조 예시 [html 파일 참고]

### Text Structure
#### HTML Text structure
- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

#### HTML [HyperText Markup Language]
- 웹 페이지의 의미와 구조를 정의하는 언어

#### `<h1>Heading</h1>`
- h1요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것

#### 대표적인 HTML Text Structure
- Heading & Paragraphs
  - h1~6, p
- Lists
  - ol, ul, li
- Emphasis & Importance
  - em(글자 눕힘), string(굵기)

#### HTML Text Structure 예시
```HTML
<body>
  <h1>Main Heading</h1>
  <h2>Sub Heading</h2>
  <p>This is my page</p>
  <p>This is <em>emphasis</em></p> 
  <p>Hi <strong>my name</strong> is Air</p>
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ol>
</body>
```

## 웹 스타일링
### CSS
#### CSS(Cascading Style Sheet)
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어

#### CSS를 적용하지 않은 웹 사이트 모습
![CSS 적용X](../00_startcamp/이미지/CSS%20적용X.png)

#### CSS 구문
```CSS
h1 {
  color: red;
  font-size: 30px;
}
```
- 선택자(Selector) : `h1 {  }`
- 선언(Declaration) : `color: red;`
- 속성(Property) : `font-size`
- 값(Value) : `30px`

#### CSS 적용 방법
1. 인라인(Inline) 스타일
2. 내부(Internal) 스타일 시트 <-- 주로 사용할 예정
3. 외부(External) 스타일 시트

#### 1. 인라인(Inline) 스타일 [사용X]
- HTML 요소 안에 style 속성 값으로 작성

#### 2. 내부(Internal) 스타일 시트
- head 태그 안에 style 태그 작성
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      ...
      <title>Document</title>
      <style>
        h1 {
          color : blue;
          background-color: yellow;
        }
      </style>
    </head>
  ```
#### 3. 외부(External) 스타일 시트
- 별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
- p.48

### CSS 선택자
#### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

#### CSS Selectors 종류
- 기본 선택자
  - 전체(*) 선택자
  - 요소(tag) 선택자
  - 클래스(class) 선택자
  - 아이디(id) 선택자
  - 속성(attr) 선택자 등

- 결합자(Combinators)
  - 자손 결합자(" "(space))
    - 첫 번째 요소의 자손 요소들 선택
    - (예) p span은 <p> 안에 있는 모든 <span>를 선택 (하위 레벨 상관 없이)
  - 자식 결합자(">")
    - 첫 번째 요소의 직계자식만 선택
    - (예) ul > li은 <ul> 안에 있는 모든 <li>를 선택 (한 단계 아래 자식들만)

#### CSS Selectors 특징
- 전체 선택자(*)
  - HTML 모든 요소를 선택
- 요소 선택자
  - 지정한 모든 태그를 선택
- 클래스 선택자('.'(dot))
  - 주어진 클래스 속성을 가진 모든 요소를 선택
- 아이디 선택자('#')
  - 주어진 아이디 속성을 가진 요소 선택
  - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
- <<04-css-selectors.html 파일 참고>>

### 명시도
#### Specificity (명시도)
- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
  - 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우, 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨

#### CSS(Cascading Style Sheet)
  - 웹 페이지의 디자인과 레이아웃을 구성하는 언어

#### Cascade (계단식)
  - 한 요소에 동일한 가중치를 가진 선택자가 적용될 때, CSS에서 마지막에 나오는 선언이 사용

#### Cascade 예시
- h1 태그 내용의 색은 purple이 적용됨
```CSS
  h1 {
    color: red;
  }
  
  h1 {
    color: purple;
  }
```

#### 명시도 적용 예시
- 동일한 h1 태그에 다음과 같이 스타일이 작성된다면 h1 태그 내용의 색은 red 적용
```CSS
.make-red {
  color: red;
}

h1 {
  color: purple;
}
```

#### 명시도가 높은 순
1. Importance
  - !important
2. Inline 스타일
3. 선택자
  - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 선언 순서

#### 명시도 예시
- p.69

#### `!important`
- 다른 우선순위 규칙보다 우선하여 적용하는 키워드
- Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음
- debugging할 때 사용

### 상속
#### CSS 상속
- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

#### CSS 속성 2가지 분류
- 상속되는 속성
  - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속되지 않는 속성
  - Box model 관련 요소(width, height, border, box-sizing ...)
  - position 관련 요소(position, top/right/bottom/left, z-index) 등

## CSS Box Model
### 개요
#### CSS Box Model
- 웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

### 박스 타입
#### 박스 타입
1. Block box
2. Inline box
- 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

#### 박스 표시(Display) 타입
1. Outer display type
2. Inner display type

#### Outer display type
1. Block & Inline
```CSS
.index {
  display: block;
}

.index {
  display: inline;
}
```
- 박스가 문서 흐름에서 어떻게 동작할지를 결정
- 속성
  - block, inline

#### Outer display type - block 특징
- 항상 새로운 행으로 나뉨
- width와 height 속성 사용 가능
- padding, margin, vorder로 인해 다른 요소를 상자로부터 밀어냄
- width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
  - 상위 컨테이너 너비 100%로 채우는 것
- 대표적인 block 타입 태그
  - h1~6, p, div

#### Outer display type - inline 특징
- 새로운 행으로 넘어가지 않음
- width와 height 속성을 사용할 수 없음
- 수직 방향
  - padding, margin, border가 적용되지만 다른 요소를 밀어낼 수 없음
- 수평 방향
  - padding, margin, border가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그
  - a, img, span, strong, em

#### Normal flow
- 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우, 웹 페이지 요소가 배치되는 방식

## 참고
### HTML 스타일 가이드
#### HTML 스타일 가이드
- 대소문자 구분
  - HTML은 대소문자를 구분하지 않지만, 소문자 사용을 강력히 권장
  - 태그명과 속성명 모두 소문자로 작성
- 속성 따옴표
  - 속성 값에는 큰 따옴표("")를 사용하는 것이 일반적
- 코드 구조와 포맷팅
  - 일관된 들여쓰기를 사용(보통 2칸 공백)
  - 각 요소는 한 줄에 하나씩 작성
  - 중첩된 요소는 한 단계 더 들여쓰기
- 공백 처리
  - HTML은 연속된 공백을 하나로 처리
  - Enter키로 줄 바꿈을 해도 브라우저에서 인식X
    - 줄 바꿈 태그를 사용해야 함
- 에러 출력 없음
  - HTML은 문버 오류가 있어도 별도의 에러 메시지 출력X

### CSS 스타일 가이드
#### CSS 스타일 가이드
- 코드 구조와 포맷팅
  - 일관된 들여쓰기를 사용(보통 2칸 공백)
  - 선택자와 속성은 각각 새 줄에 작성
  - 중괄호 앞에 공백 넣기
  - 속성 뒤에는 콜론(:)과 공백 넣기
  - 마지막 속성 뒤에는 세미콜론(;) 넣기
- 선택자 사용
  - class 선택자를 우선적으로 사용
  - id, 요소 선택자 등은 가능한 피할 것
    - 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
- 속성과 값
  - 속성과 값은 소문자로 작성
  - 0 값에는 단위 붙이지 않음
- 명명 규칙
  - 클래스 이름은 의미 있고 목적을 나타내는 이름 사용
  - 케밥 케이스(kebab-case) 사용
  - 약어보다는 전체 단어 사용
- CSS 적용 스타일
  - 인라인(inline) 스타일은 되도록 사용X
    - CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦

#### CSS의 모든 속성 외우기X
- 자주 사용되는 속성은 그리 많지 않으며 주로 활용하는 속성 위주로 사용하다 보면 자연스럽게 익히게 됨
- 그 외 속성들은 개발하며 필요할 때마다 검색해서 학습 후 사용할 것

### MDN
#### MDN Web Docs
- Mozilla Develop Network에서 제공하는 온라인 문서
- 웹 개발자와 디자이너를 위한 종합적인 참고 자료
- HTML, CSS, JavaScript, 웹 API, 개발 도구 등 웹 기술에 대한 정보를 제공

#### MDN 문서를 활용해야 하는 이유
- 정확성 및 신뢰성
  - Mozilla와 웹 커뮤니티의 전문가들에 의해 작성되고 유지 관리
  - 웹 표준을 정확하게 반영하고 있으며, 신뢰할 수 있는 정보 소스를 제공
- 최신 웹 기술
  - 최신 웹 표준과 기술을 다루고 있어, 웹 갭라자들이 최신 정보를 쉽게 접할 수 있음
- 명확한 설명과 예제
  - 복잡한 개념을 이해하기 쉽게 설명하고, 실습 가능한 예제 코드 제공

#### MDN 문서 결론
- MDN 문서는 웹 개발 학습의 모든 단계에서 중요한 참고 자료
- 개발 과정에서 발생하는 다양한 문제에 대한 솔루션을 찾는 데 유용
- 이 문서를 활용함으로써 웹 기술에 대한 깊은 이해를 얻고, 실무에 필요한 능력을 갖출 수 있음