from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from app.models.schemas.user import UserResponse, UserCreateRequest
from app.services.user_service import UserService
# create user
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
async def create_user_api(user_create_request: UserCreateRequest):
    user_service = UserService()
    user_response=user_service.create_user(name=user_create_request.name, email=user_create_request.email)
