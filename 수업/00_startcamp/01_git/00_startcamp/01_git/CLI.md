# Command Line Interface

## 1. 문법 및 활용
### (1) CLI에서 '.'(점)의 역할
- '**.**' : 현재 디렉토리 (예 : 01_git)
- '**..**' : 현재의 상위 디렉토리(부모 폴더) (예 : 00_startcamp)

### (2) 기초 문법
- touch {name}
  - 파일 생성
  - 파일이름 : **공백, 기호, 한글 X** (_는 가능)
  - 예 : touch some_file.txt
- mkdir {name}
  - 새 디렉토리 생성
  - make directory의 약자
  - 예)
     ```bash
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/
    $ mkdir 02_git_adv
    ```
- ls
  - 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
  - 예 : ls -a [숨김파일이 생기기 시작할 때 -a 사용]
    - '-'~ : 옵션
  - 예 : ls -al [리스트형태로 보여주는 문법]
- cd
  - 현재 작업 중인 디렉토리를 변경 (위치 이동)
  - 예)
    ```bash
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/01_git
    $ cd 02_git_adv/
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/02_git_adv
    $
    ```
    ```bash
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/02_git_adv
    $ cd../01_git/
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/01_git
    $
    ```
- start
  - 폴더/파일을 열기
  - 예 : code .
  - 예 : `start GIT.md`
- rm
  - 파일 삭제(디렉토리 삭제는 -r 옵션을 추가 사용)
  - rm 이용 시, 휴지통이 아닌 바로 삭제
  - 예)
     ```bash
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/02_git_adv
    $ rm some_file.txt
    SSAFY@DESKTOP-763H707 MINGW64 ~/Desktop/study/00_startcamp/01_git
    $
    ```
## **CLI에서 가장 중요한 것** : **경로**
## **절대 경로**
  - Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
  - 윈도우 바탕 화면의 절대 경로 예시
    - `C:/Users/ssafy/Desktop`
## **상대 경로**
  - 현재 작업하고 있는 디렉토리를 기준으로 게산된 상대적 위치를 작성한 것
  - 만약 현재 작업하고 있는 디렉토리가 `C:/Users`일 때 윈도우 바탕으로의 상대 경로 : `ssafy/Desktop`

