from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Blog_models(Base):
      __tablename__ = 'blogs'

      id = Column(Integer, primary_key=True, index=True)
      title = Column(String)
      body = Column(String)
      user_id=Column(Integer,ForeignKey('users.id'))
      creator=relationship("user_models", back_populates="blogs")


class user_models(Base):
      __tablename__ = 'users'

      id = Column(Integer, primary_key=True, index=True)
      name = Column(String)
      email = Column(String)     
      password = Column(String) 

      blogs=relationship("Blog_models", back_populates="creator")