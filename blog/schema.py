from pydantic import BaseModel

class blog_schema(BaseModel):
    title: str
    body: str





class User_schema(BaseModel):
      name: str
      email: str
      password:str

class showUser_schema(BaseModel):
      name: str
      email: str


      class Config():
          orm_mode=True      


class showblog_schema(BaseModel):
    title: str
    body: str
    creator:showUser_schema

    
    class Config():
          orm_mode=True

class login_schema(BaseModel):
      username: str
      password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
     email: str | None = None
    #  username:optional[str]=None      

