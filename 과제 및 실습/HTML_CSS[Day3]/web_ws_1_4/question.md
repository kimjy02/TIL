# 문제
- CSS 프로퍼티는 상속이 되는 것과 되지 않는 것이 있다.
- https://poiemaweb.com/css3-inheritance-cascading를 참고하여 상속되는 프로퍼티는 상속 되지 않게, 상속 되지 않는 프로퍼티는 상속 되도록 하시오.
# 요구사항
- 오직 style 태그의 내용만 수정한다. 
- inherit, border, text-align, color 를 활용한다. 
- .outer-box 의 width, height 는 자식에게 상속되지 않는다. 
- .inner-box 의 border 는 .outer-box의 속성을 상속받는다. 
- '첫 번째' span 의 색상과 정렬은 .outer-box의 속성을 상속받아 빨간색, 중앙 정렬 되어야 한다. 
- '두 번째' span 은 색상과 정렬 두 속성 모두 .outer-box로부터 상속받지 않는다. 
