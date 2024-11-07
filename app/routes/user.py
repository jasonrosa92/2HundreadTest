from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt import verify_access_token


user_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@user_router.get("/user")
def read_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload.get("role") != "user":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "User content"}
