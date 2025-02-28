# 1. Python 3.10 기반 이미지 사용
FROM python:3.12-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 패키지 목록 복사
COPY requirements.txt /app/requirements.txt

# 4. 패키지 설치
RUN pip install --no-cache-dir -r /app/requirements.txt

# 5. 전체 소스 코드 복사
COPY . /app

# 6. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]