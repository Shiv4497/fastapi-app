
from fastapi import FastAPI,Depends,status,Response,HTTPException
from schema import blog_schema, showblog_schema,User_schema,showUser_schema
from models import Base,Blog_models,user_models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from hashing import hash



def get_all(db:Session):
    blogs=db.query(Blog_models).all()
    return blogs


def show(id :int, db:Session):
    blog=db.query(Blog_models).filter(Blog_models.id == id).first()
    if not blog:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
    return blog


def create(request:blog_schema,db:Session):
    new_blog = Blog_models(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    

def destroy(id:int,db:Session):
   blog= db.query(Blog_models).filter(Blog_models.id ==id)
   blog.delete(synchronize_session=False)
   db.commit()
   return 'Done'

def update(id:int, request:blog_schema,db:Session):
   var= db.query(Blog_models).filter(Blog_models.id ==id).first()
   if not var:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
   var.title=request.title
   var.body=request.body
   db.commit()
   db.refresh(var)
   return 'updated'