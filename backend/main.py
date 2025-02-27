from datetime import datetime
from typing import Callable
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pytz import timezone
from com.jinmini.auth.admin.web.admin_router import router as admin_router
from com.jinmini.carbon.web.carbon_router import router as carbon_router
from com.jinmini.auth.user.web.user_router import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags = ["User"])
app.include_router(admin_router, prefix="/admin", tags = ["Admin"])
app.include_router(carbon_router, prefix="/carbon", tags = ["Carbon"])

current_time: Callable[[], str] = lambda: datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
    <h2>{current_time()}</h2>
</div>
</body>
""")
                  
# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 