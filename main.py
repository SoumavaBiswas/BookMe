from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.AdminBookTransaction import AdminBookTransactionRouter
import time
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

origins = [
    "http://localhost:3000"
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Processed {request.url.path} in {str(process_time)} seconds.")
    return response



app.include_router(AdminBookTransactionRouter, tags=["Books"])