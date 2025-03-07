from datetime import datetime
from typing import Callable
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from pytz import timezone
import asyncpg
from com.jinmini.design_pattern.creational.builder.db_builder import get_db

app = FastAPI()

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

@app.get("/users")
async def get_users(db=Depends(get_db)):
    print("😎😀➕ get/users로 진입")
    query = "SELECT * FROM member"
    try:
        result = await db.fetch(query)
        return {"users":[dict(record) for record in result]}
    except Exception as e:
        print(f"⚠️ 데이터 조회 중 오류 발생:", {str(e)})
        return {"error": "데이터 조회 중 오류 발생"}


    
# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 
# curl http://localhost:8000

