from fastapi.encoders import jsonable_encoder
from helping.user import HelpingUser


def get_user_schema(entity):
    cpf = HelpingUser.show_cpf(entity.get('cpf'))
    return jsonable_encoder({
        'id': str(entity.get('_id')),
        'full_name': f'{str(entity.get("first_name"))} {str(entity.get("last_name"))}',
        'username': str(entity.get('username')),
        'email': str(entity.get('email')),
        'cpf': str(cpf)
    })

def get_users_schema(entities):
    return jsonable_encoder([get_user_schema(entity) for entity in entities])
