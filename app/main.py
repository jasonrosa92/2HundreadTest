from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.auth.jwt import create_access_token, verify_access_token
from app.auth.utils import verify_password, get_password_hash


fake_users_db = {
    "user": {
        "username": "user",
        "role": "user",
        "password": get_password_hash("L0XuwPOdS5U")  # Senha hashada
    },
    "admin": {
        "username": "admin",
        "role": "admin",
        "password": get_password_hash("JKSipm0YH")  # Senha hashada
    },
}

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user['password']):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload["role"] != "admin":
        raise HTTPException(status_code=403, detail="Insufficient privileges")
    return payload

@app.get("/user")
def read_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload.get("role") != "user":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "User content"}

@app.get("/admin")
def read_admin(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "Admin content"}
