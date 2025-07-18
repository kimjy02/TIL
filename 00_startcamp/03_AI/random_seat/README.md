# 랜덤 자리 배치 프로그램

이 프로젝트는 28명의 학생을 2분단, 총 28자리에 랜덤하게 배치하는 프로그램입니다.

## 폴더 구조
- data/ : 명단 파일(txt, xlsx 등)
- src/ : 소스 코드
- output/ : 결과 파일(표, 이미지 등)

## 시작 방법
1. data 폴더에 명단 파일(students.txt 또는 students.xlsx)을 준비합니다.
   - students.txt: 한 줄에 한 명씩 이름 작성
   - students.xlsx: A열에 이름 작성
2. (엑셀 파일 사용 시) openpyxl 패키지 설치
   - 명령어: pip install openpyxl
3. src 폴더에서 아래 명령어로 실행
   - python assign_seat.py
4. 결과는 콘솔과 output/seat_result.txt에 출력됩니다.

워크플로우와 예시는 상위 폴더의 README_seat.md를 참고하세요.
