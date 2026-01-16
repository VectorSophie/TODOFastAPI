import logging
from typing import Dict, Any
from app.exceptions import EmailNotAllowedNameExistsError

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self):
        pass

    def _valid_email(self, email: str) -> bool:
        logger.info(f"email valid check: {email}")
        if email == "admin@example.com":
            raise EmailNotAllowedNameExistsError(email)
        return True

    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        if not self._valid_email(email):
            raise ValueError("Invalid email format")
        # save 추가
        return {'id': 1, 'name': name, 'email': email}