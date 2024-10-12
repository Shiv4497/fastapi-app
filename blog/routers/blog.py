from fastapi import APIRouter,Depends,status,Response,HTTPException
from schema import blog_schema, showblog_schema,User_schema,showUser_schema
from models import Base,Blog_models,user_models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from hashing import hash
from repository import blog
from oaut2 import get_current_user

router=APIRouter(
    prefix="/blog",
    tags=['Blog']
    )

@router.get('/')
def all(db:Session = Depends(get_db),current_user:User_schema=Depends(get_current_user)):
    return blog.get_all(db)
    # blogs=db.query(Blog_models).all()
    # return blogs

@router.get('/{id}',response_model=showblog_schema)
def show(id:int, db:Session = Depends(get_db),current_user:User_schema=Depends(get_current_user)):
    return blog.show(id,db)
    # blog=db.query(Blog_models).filter(Blog_models.id == id).first()
    # if not blog:
    #      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
    # return blog


@router.post('/',status_code=status.HTTP_201_CREATED)
#Storing blog in database
def create(request:blog_schema, db:Session=Depends(get_db),current_user:User_schema=Depends(get_current_user)):
    return blog.create(request,db)
    # new_blog = Blog_models(title=request.title,body=request.body)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db),current_user:User_schema=Depends(get_current_user)):
    return blog.destroy(id,db)
#    blog= db.query(Blog_models).filter(Blog_models.id ==id)
#    blog.delete(synchronize_session=False)
#    db.commit()
#    return 'Done'

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)   
def blog_update(id:int, request:blog_schema, db:Session = Depends(get_db),current_user:User_schema=Depends(get_current_user)):
    return blog.update(id,request,db)
#    var= db.query(Blog_models).filter(Blog_models.id ==id).first()
#    if not var:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
#    var.title=request.title
#    var.body=request.body
#    db.commit()
#    db.refresh(var)
#    return 'updated'