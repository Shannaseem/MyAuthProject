from pydantic import BaseModel, EmailStr

# ✅ For creating a new user during signup
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

# ✅ For logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# ✅ For sending user data back in responses
class User(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        from_attributes = True  # ✅ Must be inside the class
