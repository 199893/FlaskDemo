from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
 encoding='utf8', echo=True)


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)


from sqlalchemy import Column,Integer,String,ForeignKey


class User(Base):
     __tablename__ = "user"
     id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
     username = Column(String(20),nullable=False)
     password = Column(String(50),nullable=False)

class Data(Base):
    __tablename__='data'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name=Column(String(50),nullable=False)
    desc=Column(String(500),nullable=False)
    userid=Column(Integer,ForeignKey('user.id',ondelete='CASCADE'))

if __name__=='__main__':
    '''创建表'''
    Base.metadata.create_all(bind=engine)