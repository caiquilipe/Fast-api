from fastapi import FastAPI

from routes.user import user_routes


app = FastAPI()
app.include_router(user_routes)