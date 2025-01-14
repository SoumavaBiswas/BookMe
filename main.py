from fastapi import FastAPI
from  Routers.AdminBookTransaction import AdminBookTransactionRouter

app = FastAPI()

app.include_router(AdminBookTransactionRouter, tags=["Books"])