# Component State Flow
<details>
<summary>Index</summary>

1. Passing Props
  - Props
  - Props 활용

2. Component Events
  - Emit
  - 이벤트 발신 및 수신
  - emit 이벤트 활용

3. Computed Properties
  - Computed
  - Computed vs. Method

4. Watchers
  - Watch
  - computed vs. watch

</details>

## 1. Passing Props
### 1) Props
#### 같은 데이터 하지만 다른 컴포넌트
- 동일한 사진 데이터가 한 화면에 다양한 위치에서 여러 번 출력되고 있음
- 하지만 해당 페이지를 구성하는 컴포넌트가 여러 개라면 각 컴포넌트가 개별적으로 동일한 데이터를 관리해야 할까?
- 그렇다면 사진을 변경해야 할 때 모든 컴포넌트에 대해 변경 요청을 해야 함
- > "공통된 부모 컴포넌트에서 관리하자"

- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)

#### Props
- 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는 데 사용되는 속성

#### Props 특징
- 부모 속성이 업데이트되면 자식으로 전달되지만 그 반대는 안됨
- 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
- 또한 부모 컴포넌트가 업데이트될 때마다 이를 사용하는 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨
- > 부모 컴포넌트에서만 변경하고 이를 내려 받는 자식 컴포넌트는 자연스럽게 갱신

#### One-Way Data Flow
- 모든 props는 자식 속성과 부모 속성 사이에 <span style='color:red'>히향식 단방향 바인딩</span>을 형성(one-way-down binding)

#### 단방향인 이유
- 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함
- > 데이터 흐름의 '일관성' 및 '단순화'

### 2) Props 선언
#### 사전 준비
1. vue 프로젝트 생성
2. 초기 생성된 컴포넌트 모두 삭제(App.vue 제외)
3. src.assets 내부 파일 모두 삭제
4. main.js 해당 코드 삭제
    `import './assets/main.css'`
5. App > Parent > ParentChild 컴포넌트 관계 작성
6. App 컴포넌트 작성
   ```vue
   <!-- App.vue -->

   <template>
        <div>
            <Parent />
        </div>
    </template>

    <script setup>
    import Parent from '@/components/Parent.vue'
    </script>
    ```
7. Parent 컴포넌트 작성
   ```vue
   <!-- Parent.vue -->

   <template>
        <div>
            <ParentChild />
        </div>
    </template>

    <script setup>
    import ParentChild from '@/components/ParentChild.vue'
    </script>
    ```

    
