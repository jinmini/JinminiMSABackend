from fastapi import FastAPI
from com.jinmini.auth.admin.admin_router import router as admin_router
from com.jinmini.auth.user.user_router import router as user_router

# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 

app = FastAPI()

app.include_router(user_router, prefix="/user", tags = ["User"])
app.include_router(admin_router, prefix="/admin", tags = ["Admin"])
                   
@app.get("/")
def read_root():
    return {"main":"메인 라우터"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)