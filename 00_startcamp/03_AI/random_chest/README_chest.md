# 랜덤 사물함 자리 배치 프로그램 워크플로우

## 목적
28명의 학생을 1~4줄, 가로 7개씩(총 28개)에 랜덤하게 사물함을 배정하는 프로그램을 만듭니다. (5번째 줄은 사용하지 않음)

## 입력 데이터
- 28명의 명단이 담긴 텍스트 파일(.txt) 또는 엑셀 파일(.xlsx)

## 워크플로우
1. **명단 파일 준비**
    - 학생 이름이 한 줄에 하나씩 적힌 텍스트 파일 또는 엑셀 파일을 준비합니다.
2. **명단 불러오기**
    - 프로그램에서 파일을 읽어 28명의 이름을 리스트로 저장합니다.
3. **사물함 구조 정의**
    - 1~4줄, 가로 7개씩(총 28개) 사물함 구조를 정의합니다.
    - 5번째 줄은 사용하지 않습니다.
4. **사물함 랜덤 배정**
    - 28명의 명단을 무작위로 섞어 사물함 구조에 맞게 배정합니다.
5. **결과 출력**
    - 사물함 배치 결과를 표 형태로 출력하거나 파일로 저장합니다.

## 확장 기능(선택)
- 사물함 배치 결과를 이미지로 저장
- 특정 학생을 특정 사물함에서 제외/고정
- 사물함 배치 이력 저장

---


# 예시

```
□1 □2 □3 □4 □5 □6 □7
□8 □9 □10 □11 □12 □13 □14
□15 □16 □17 □18 □19 □20 □21
□22 □23 □24 □25 □26 □27 □28
```

