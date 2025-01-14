from fastapi import FastAPI
from  RestAPI.AdminBookTransaction import AdminBookTransactionRouter

app = FastAPI()

app.include_router(AdminBookTransactionRouter, tags=["Books"])