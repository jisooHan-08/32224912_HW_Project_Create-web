# 1. Python 3.10 기반 이미지 사용
FROM python:3.10-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 파일 복사
COPY requirements.txt /app/

# 하위 폴더와 코드 직접 복사
COPY hw_project_buildweb/ hw_project_buildweb/
COPY vote_evalu_project/ vote_evalu_project/
COPY templates/ templates/
COPY manage.py /app/

# 4. 패키지 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
