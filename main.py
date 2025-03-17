from datetime import datetime
from typing import Callable
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from pytz import timezone
import asyncpg
from com.jinmini.app_router import router as app_router

app = FastAPI()
app.include_router(app_router)

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

