from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt import verify_access_token


admin_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@admin_router.get("/admin")
def read_admin(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "Admin content"}
