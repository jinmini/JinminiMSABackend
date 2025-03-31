# 1. Python 3.12 기반 이미지 사용
FROM python:3.12-slim

# 필수 패키지 설치
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 2. 작업 디렉토리 설정
WORKDIR /backend

# 3. 필요한 패키지 목록 복사
COPY requirements.txt .

# 4. 패키지 설치 (패키지 충돌 문제 해결)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir python-jose[cryptography] passlib[bcrypt] redis[asyncio]

# 5. 전체 소스 코드 복사
COPY . /backend/

# Python 실행 경로 설정
ENV PYTHONPATH="/backend"

# 6. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 