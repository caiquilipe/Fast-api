from schemas.user import get_user_schema, get_users_schema
from validate.user import UserValidation
from helping.user import HelpingUser
from models.user import User
from config.db import db

from fastapi.responses import JSONResponse
from fastapi import APIRouter, status

from bson import ObjectId


user_routes = APIRouter()

@user_routes.get('/users')
async def find_all_users():
    response = get_users_schema(db.user.find())
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@user_routes.get('/users/{id}')
async def find_one_user(id: str):
    response = get_user_schema(db.user.find_one({'_id': ObjectId(id)}))
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@user_routes.post('/users')
async def create_user(user: User):
    user = dict(user)
    UserValidation.validate_username(user.get('username'))
    UserValidation.validate_email(user.get('email'))
    user['password'] = HelpingUser.hide_password(user.get('password').encode('utf-8'))
    user['cpf'] = UserValidation.validate_cpf(user.get('cpf'))
    created = db.user.insert_one(user)
    response = get_user_schema(db.user.find_one({'_id': ObjectId(created.inserted_id)}))
    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)
