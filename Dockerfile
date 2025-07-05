# 1. Python 3.10 기반 이미지 사용
FROM python:3.10-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. mysqladmin 설치 
RUN apt-get update && apt-get install -y default-mysql-client

# 4. requirements.txt 먼저 복사하고 패키지 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. 나머지 코드 복사
COPY hw_project_buildweb/ hw_project_buildweb/
COPY vote_evalu_project/ vote_evalu_project/
COPY templates/ templates/
COPY manage.py /app/

# 6. Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
