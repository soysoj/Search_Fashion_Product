from fastapi import FastAPI
from app.routes import router as app_router
import uvicorn

app = FastAPI()

# 라우터 등록
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)