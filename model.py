import mysqlobject as m
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
 encoding='utf8', echo=True)

from sqlalchemy.orm import sessionmaker
session=sessionmaker()()

def inserUser(username,password):
    result=session.add(m.User(username=username,password=password))
    session.commit()
    session.close()
    print(result)

def checkUser(username,password):
    result=session.query(m.User).filter(m.User.username==username).filter(m.User.password==password).first().id
    if result:
        return result
    else:
        return -1

def lookUser(username):
    result=session.query(m.User.id).filter(m.User.username==username).first()
    if result:
        return result
    else:
        return -1


def inserData(name,desc,userid):
    result=session.add(m.Data(name=name,desc=desc,userid=userid))
    session.commit()
    session.close()
    print("------------------",result)

def checkData(userid):
    result = session.query(m.Data.id,m.Data.name,m.Data.desc).filter(m.Data.userid==userid).all()
    if result:
        return result
    else:
        return -1

def delData(id):
    result = session.query(m.Data).filter(m.Data.id==id).delete()
    session.commit()
    session.close()
    print(result)

def ameData(id,ame):
    result = session.query(m.Data).filter(m.Data.id==id).first().name=ame
    session.commit()
    session.close()
    print(result)

def ameData1(id,ame):
    result = session.query(m.Data).filter(m.Data.id==id).first().desc=ame
    session.commit()
    session.close()
    print(result)

