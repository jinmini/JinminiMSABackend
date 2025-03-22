from datetime import datetime
from typing import Callable
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pytz import timezone
from com.jinmini.app_router import router as app_router

app = FastAPI()

# CORS 설정 - 개발 환경에서 허용할 출처 명시적 지정
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js 개발 서버
        "http://localhost",
        "http://127.0.0.1:3000",
        "http://127.0.0.1",
        "http://192.168.0.1:3000" # 필요한 경우 개발용 IP 추가
    ],
    allow_credentials=True,  # 쿠키 허용
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],  # 허용할 HTTP 메서드
    allow_headers=["*"],  # 모든 헤더 허용
    expose_headers=["Content-Type", "Authorization"],  # 브라우저에 노출할 헤더
    max_age=600,  # 프리플라이트 요청 캐시 시간(초)
)

app.include_router(app_router, prefix="/api")

current_time: Callable[[], str] = lambda: datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")

@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> FastAPI with Docker!</h1>
    <h2>{current_time()}</h2>
</div>
</body>
""")

# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 
# curl http://localhost:8000

