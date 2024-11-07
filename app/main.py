from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt import create_access_token, verify_access_token

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "user": {"username": "user", "role": "user", "password": "!3Ba92753$"},
    "admin": {"username": "admin", "role": "admin", "password": "admin!3Ba92753$"},
}

@app.post("/token")
def login(form_data: dict):
    user = fake_users_db.get(form_data["username"])
    if not user or user["password"] != form_data["password"]:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"], "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user")
def read_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload["role"] != "user":
        raise HTTPException(status_code=403, detail="Not authorized")
    return {"message": "Welcome, user!"}

@app.get("/admin")
def read_admin(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return {"message": "Welcome, admin!"}
