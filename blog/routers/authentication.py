from fastapi import APIRouter,Depends,status,Response,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schema import login_schema, blog_schema, showblog_schema,User_schema,showUser_schema
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from models import Base,Blog_models,user_models
from hashing import hash
from JWTtoken import create_access_token



router=APIRouter(tags=['authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(get_db)):
    user=db.query(user_models).filter(user_models.email == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Invalid Credentials")
    
    if not hash.verify(user.password,request.password):
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Incorrect password")
#     return user
    access_token = create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}  