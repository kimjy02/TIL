# 문제
- 현재 코드에서는 input#userInput에 입력한 내용이 그대로 span#output에 출력된다.
- 실행 결과를 참고하여 badWords에 포함된 단어가 사용자 입력에 포함되어 있을 경우, span#output에서 해당 단어를 **로 바꿔 출력하도록 filterMessage 함수를 완성하시오.

# 요구사항

- badWords 배열에 있는 단어가 사용자 입력에 포함되어 있으면 교체 한다.
  - forEach Array Helper Method를 활용하여 badWords배열을 순회한다.

- 같은 badWord가 여러번 등장해도 모두 교체되어야 한다.