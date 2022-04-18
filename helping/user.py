from abc import ABC, abstractclassmethod

import bcrypt


class HelpingUser(ABC):
    @abstractclassmethod
    def show_cpf(self, cpf):
        cpf_formatted = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        return cpf_formatted
    
    @abstractclassmethod
    def hide_password(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())