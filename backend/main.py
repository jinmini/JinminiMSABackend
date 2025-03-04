from datetime import datetime
from typing import Callable
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from pytz import timezone
from com.jinmini.auth.admin.web.admin_router import router as admin_router
from com.jinmini.carbon.web.carbon_router import router as carbon_router
from com.jinmini.auth.user.web.user_router import router as user_router
from database import get_db

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
    <h1> FastAPI with Docker!</h1>
    <h2>{current_time()}</h2>
</div>
</body>
""")

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    try:
        result = db.execute("SELECT version();").fetchone()
        return {"db_version": result[0]}
    except Exception as e:
        return {"error": str(e)}

# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 