import uvicorn
from fastapi import FastAPI
# from fastapi import FastAPI,Depends,status,Response,HTTPException
# from schema import blog_schema, showblog_schema,User_schema,showUser_schema
from database import Base,Blog_models,user_models
from database import engine,SessionLocal,get_db
# from sqlalchemy.orm import Session
# from hashing import hash
from routers import blog,user,authentication


Base.metadata.create_all(engine)



# Storing blog in database
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()    

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['Blog'])
# #Storing blog in database
# def create(request:blog_schema, db:Session=Depends(get_db)):
#     new_blog = Blog_models(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blog'])
# def destroy(id,db:Session = Depends(get_db)):
#    blog= db.query(Blog_models).filter(Blog_models.id ==id)
#    blog.delete(synchronize_session=False)
#    db.commit()
#    return 'Done'


# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blog'])   
# def blog_update(id, request:blog_schema, db:Session = Depends(get_db)):
#    var= db.query(Blog_models).filter(Blog_models.id ==id).first()
#    if not var:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
#    var.title=request.title
#    var.body=request.body
#    db.commit()
#    db.refresh(var)
#    return 'updated'

# @app.get('/blog',tags=['Blog'])
# def all(db:Session = Depends(get_db)):
#     blogs=db.query(Blog_models).all()
#     return blogs

# @app.get('/blog/{id}',response_model=showblog_schema,tags=['Blog'])
# def show(id, response:Response, db:Session = Depends(get_db)):
#     blog=db.query(Blog_models).filter(Blog_models.id == id).first()
#     if not blog:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
#     return blog





# @app.post('/user',response_model=showUser_schema,tags=['user'])
# def create_user(request:User_schema, db:Session = Depends(get_db)):
#     new_user=user_models(name=request.name,email=request.email,password=hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user  

# @app.get('/user/{id}',response_model=showUser_schema,tags=['user'])
# def get_user(id:int, db:Session = Depends(get_db)):
#     user_new= db.query(user_models).filter(user_models.id ==id).first()
#     if not user_new:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
#     return user_new


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
