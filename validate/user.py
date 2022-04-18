from fastapi.exceptions import HTTPException
from fastapi import status

from schemas.user import get_users_schema
from config.db import db

from abc import ABC, abstractclassmethod


class UserValidation(ABC):
    @abstractclassmethod
    # check if it exists in db
    def validate_username(self, username):
        if get_users_schema(db.user.find({'username':username})):
            raise HTTPException(detail='Username already exists.', status_code=status.HTTP_400_BAD_REQUEST)

    @abstractclassmethod
    def validate_email(self, email):
        # check if it exists in db
        if get_users_schema(db.user.find({'email':email})):
            raise HTTPException(detail='Email already exists.', status_code=status.HTTP_400_BAD_REQUEST)
    
    @abstractclassmethod
    def validate_cpf(self, cpf):
        # fetch numbers cpf
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        if not len(numbers) == 11 or len(set(numbers)) == 1:
            raise HTTPException(detail='Invalid cpf.', status_code=status.HTTP_400_BAD_REQUEST)

        # Validation of the first check digit:
        sum_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            raise HTTPException(detail='Invalid cpf.', status_code=status.HTTP_400_BAD_REQUEST)

        # Validation of the second check digit:
        sum_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            raise HTTPException(detail='Invalid cpf.', status_code=status.HTTP_400_BAD_REQUEST)

        # converting cpf to string
        cpf = ''.join([str(number) for number in numbers])

        # check if it exists in db
        if get_users_schema(db.user.find({'cpf':cpf})):
            raise HTTPException(detail='CPF already exists.', status_code=status.HTTP_400_BAD_REQUEST)
        return cpf
    