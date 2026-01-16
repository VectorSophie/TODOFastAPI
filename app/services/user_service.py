import logging
from typing import Dict, Any
from app.exceptions import EmailNotAllowedNameExistsError


class UserService:
    def __init__(self):
        pass
    def _valid_email(self,email: str) -> bool:
        logging.debug('email')
        return True
    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        if not self._valid_email(email):
            raise ValueError("Email address is not valid")
        return {'id':1,'name':name,'email':email}