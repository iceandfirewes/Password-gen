#venv\Scripts\activate.bat
#uvicorn app.main:app --reload
import random
from fastapi import FastAPI
from app.schemas import PasswordRequest
app = FastAPI()

@app.get("/")
def root():
    return "This is an API for return a random password"
@app.post("/passwords")
def generate_passwords(password_request: PasswordRequest):
    passwordArray = []
    allowableCharacter = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowableCharacter += allowableCharacter
    for i in range(password_request.count):
        password = ""
        for i in range(password_request.length):
            if(password_request.special_Character):
                allowableCharacter += "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
            password += random.choice(allowableCharacter)
        passwordArray.append(password)
    return passwordArray
@app.get("/passwords")
def generate_password():
    tempPasswordRequest =  PasswordRequest()
    return generate_passwords(tempPasswordRequest)