from fastapi import APIRouter,Depends,status,Response,HTTPException
from schema import blog_schema, showblog_schema,User_schema,showUser_schema
from models import Base,Blog_models,user_models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from hashing import hash
from repository import user

router=APIRouter(
    prefix="/user",
    tags=['user']
    )

@router.post('/',response_model=showUser_schema)
def create_user(request:User_schema, db:Session = Depends(get_db)):
     return user.create(request,db)
    # new_user=user_models(name=request.name,email=request.email,password=hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user  

@router.get('/{id}',response_model=showUser_schema)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_user(id,db) 
    # user_new= db.query(user_models).filter(user_models.id ==id).first()
    # if not user_new:
    #      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
    # return user_new
