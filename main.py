from time import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from models.urbanizations import create_db_and_tables
from routes.routes import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Create all data bases and tables
create_db_and_tables()
app.include_router(router, prefix = "/auth", tags=["Authentication"])