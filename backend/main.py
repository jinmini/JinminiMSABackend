from datetime import datetime
from typing import Callable
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from pytz import timezone
from com.jinmini.design_pattern.creational.singleton.db_singleton import db_singleton
import asyncpg
# from database import get_db

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
async def get_users():
    print("😎😀➕ get/users로 진입")

    try:
        # 비동기 데이터베이스 연결 생성
        conn = await asyncpg.connect(db_singleton.db_url)
        
        query = "SELECT * FROM member"
        rows = await conn.fetch(query)
        
        result = [dict(row) for row in rows]
    
        await conn.close()
        
        return result
    except Exception as e:
        print(f"⚠️ 데이터베이스 쿼리 실행 중 오류 발생: {str(e)}")
        return {"error": str(e)}

@app.get("/db-test")
async def test_db_connection():
    """데이터베이스 연결을 테스트하는 엔드포인트"""
    db_singleton = DataBaseSingleton()
    
    # 연결 정보 출력
    connection_info = {
        "hostname": db_singleton.db_hostname,
        "port": db_singleton.db_port,
        "database": db_singleton.db_database,
        "username": db_singleton.db_username,
        "url": db_singleton.db_url.replace(db_singleton.db_password, "********")  # 비밀번호 가림
    }
    
    try:
        # 연결 테스트
        conn = await asyncpg.connect(db_singleton.db_url)
        await conn.execute("SELECT 1")  # 간단한 쿼리 실행
        await conn.close()
        
        return {
            "status": "success",
            "message": "데이터베이스 연결 성공",
            "connection_info": connection_info
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": f"데이터베이스 연결 실패: {str(e)}",
            "connection_info": connection_info
        }
    

# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 
# curl http://localhost:8000

