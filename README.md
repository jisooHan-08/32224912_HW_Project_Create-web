# 32224912_HW_Project_Create-web

## 프로젝트 개요
Django와 Docker를 활용한 웹사이트로, 프로젝트를 생성하고 사용자가 평가할 수 있는 투표 시스템을 구축하였습니다.

## 요구 기능:
- 관리자는 프로젝트 주제와 상세 내용을 등록할 수 있어야 함
- 사용자는 프로젝트 리스트에서 프로젝트를 선택해 상세 내용 확인 후, 1~5점으로 평가 가능
- 사용자는 평가 제출 후 결과(평균 점수)를 확인 가능
- 관리자는 모든 프로젝트의 평균 점수를 기준으로 정렬된 결과 확인 가능
- Docker, Mysql, GitHub 활용 포함 필수

## 구현한 주요 기능
- 관리자
  - 프로젝트 주제 및 상세 내용 등록 가능하다.
- 사용자
  - 초기 페이지에서 프로젝트 작성, 프로젝트 평가 리스트, 현재 프로젝트 평가 현황을 확인 할 수 있다
  - 프로젝트 평가 리스트 페이지에서 프로젝트 선택 후 1~5점 평가 
  - 투표 완료 후 결과 확인 가능
  - 최종 평가 결과 페이지로 이동 가능
  - 다시 초기 페이지로 이동 가능
- 정렬 기능
  - 평균 점수 순으로 프로젝트 정렬

## 프로젝트 파일 구조
HW_PROJECT_BUILDWEB/  # 전체의 루트 설정 폴더로, Django 설정 파일들이 들어있다.
 - hw_project_buildweb/               # Django 프로젝트 설정 폴더
 - settings.py, urls.py 등         # 필수 설정 포함
   
vote_evalu_project/               # 앱 폴더: 핵심 디렉토리
  - models.py                      # Project, Evaluation 모델
  - views.py, forms.py             # 평가 기능 및 폼 처리
  - admin.py                       # 관리자 등록
  - migrations/                    # 마이그레이션 포함됨

templates/vote_evalu_project/     # 템플릿: HTML 파일들
  - home.html                      # 초기화면
  -  create_project.html           # 관리자 등록 페이지
  -  project_list.html             # 프로젝트 목록
  -  project_detail.html           # 평가 상세
  -  sorted_project_list.html      # 평균순 정렬
  -  project_success.html          # 평가 완료

Dockerfile                        # Django 서버용 Docker 설정
 - docker-compose.yml               # 서비스 통합 실행 설정
 - requirements.txt                 # Django 등 패키지 정의
 - manage.py                        # Django 실행 진입점
 - .gitignore                       # 불필요 파일 제외 설정



## 주요 URL
- `/` : 초기 홈 화면
- `/project/create/` : 프로젝트 생성 ( 관리자 )
- `/projects/` : 평가 가능한 프로젝트 목록
- `/projects/sorted/` : 평균 점수 순 정렬
- `/projects/<id>/` : 프로젝트 상세 페이지 및 평가 페이지

## 실행 방법 (Docker 사용)

docker-compose build
docker-compose up

→ 브라우저에서 ( http://localhost:8000/ ) 접속







