# Git
## Git
- 분산 **버전 관리 시스템**
  - 버전 관리 : 변화를 기록하고 추적하는 것
    - **버전 관리 반드시 해야 함**
    ![집 버전 관리](./house.png)
  - **중앙 vs. 분산** 
    - 중앙 집중식
      - 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드
      ![중앙 집중식](./center.png)
    - 분산식
      - 버전을 여러 개의 복제된 저장소에 저장 및 관리
      - 중앙 서버를 사용하지 못하는 상황이라도, 복제된 다른 저장소를 이용해 파일 사용 가능
      - 예)
        - A : 파란색 창문으로 바꿈
        - B : 빨간색 창문으로 바꿈
        - ver5를 만들 때는 원본을 바탕으로 만듦
      - 중앙 서버에 의존하지 않고도 동시에 다양한 작업 수행 가능
        - 개발자 간의 작업 충돌 ↓, 개발 생산성 ↑
      - 중앙 서버의 장애느 손실에 대비해 백업과 복구 용이
      -인터넷에 연결되지 않은 환경에서도 작업 계속 가능
        - 변경 이력과 코드를 로컬 저장소에 기록 / 나중에 중앙 서버와 동기화

        ![분산식](./var.png)

## Git의 영역
### 1. Working Directory
- 실제 작업 중인 파일들이 위치하는 영역
### 2. Staging Area
- Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
### 3. Repository
- 버전(**Commit**) 이력과 파일들이 영구적으로 저장되는 영역
- 모든 버전과 변경 이력이 기록됨
- Repository에 저장되면 Staging Area는 비워짐(?)
### Commit("버전")
- 변경된 파일들을 저장하는 행위
- 마치 사진을 찍듯이 기록한다 하여 'snapshot'이라고도 함

## Git의 동작
1. git init
  - 로컬 저장소 설정(초기화)
  - git의 버전 관리를 시작할 디렉토리에서 진행
  ![folder](/folder_study.png)
  - `$ git init`
2. git add
  - 변경사항이 있는 파일을 staging area에 추가
  - `$git add 00_startcamp/01_git/markdown.md`
  - 아래 명령어로 저장된 파일과 저장되지 않은 파일 확인
  ![git status](/git%20status.png)
  - staging area에 저장된 파일 수정 시, `git status` 입력 시 변경된 사항 설명됨
  - 실수로 필요없는 파일 추가로 인해 제거해야 할 상황
    - `git restore --staged <file>...`
3. git commit
  - staging area에 있는 파일들을 저장소에 기록
  - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
  - `git commit` 오류 코드

    ![git commit](/git%20commit%20오류%20코드.png)
  - `git config --global user.email "02kimjy@naver.com"`
  - `git config --global user.name "김주연"`
  - `git config --global --list`
  - `--global`로 저장해서 컴퓨터 자체에 저장되어 있으므로 한 번만 입력해도 됨
  - 여러 개의 계정으로 git을 관리해야 할 경우, local로 이용(찾아보기)

    ![git commit](/git%20commit%20코드.png)
  - `code ~/.gitconfig` : 이메일과 이름 수정 코드

## **git은 로컬 저장소 내 모든 파일의 '변경사항'을 감시하고 있다.**

## Remote Repository
### 원격 저장소
- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장
- 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
- #### 다양한 원격 저장소 서비스
  - GitLab(SSAFY에서 사용, 프라이빗) : 프로젝트 생성할 때마다 강사님 초대
  - GitHub(포트폴리오용, 공개적) : 
  - Bitbucket

## 로컬 & 원격 저장소
1. `git remote add origin url`
  - url을 origin이라는 이름으로 추가
  
2. `git pull`
  - 가져오기
- 순서
  1. `git init`
  2. 작업
  3. `git add`
  4. `git commit`
  5. `git push`
  6. `git pull`

**commit 이름 설정 시, 수정사항이 무엇인지, 주 목적이 무엇인지 표현하기**
