'''
flask模块引用
'''
from flask import Flask,render_template,request,redirect,make_response
import datetime
import mysqlobject
import model

app=Flask(__name__)
app.send_file_max_age_default=datetime.timedelta(seconds=1)
app.debug=True

#将http//127.0.0.1:5000和index视图函数绑定
@app.route('/')
def jmx():
    user=request.cookies.get('name')
    # pwd=model.lookUser(user)
    # print(pwd[0])
    return render_template('jmx.html',userinfo=user)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        print('收到get请求，注册返回界面')
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        # print(username,password)
        # print('收到post请求，提取表单参数')
        try:
            model.inserUser(username,password)
            return redirect('/register')
        except:
            redirect('/login')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='GET':
        print('收到get请求，登录返回界面')
        return render_template('register.html')
    elif request.method=='POST':

        username=request.form['username']
        password=request.form['password']
        # print(username,password)
        # print('收到post请求，验证账号密码')
        try:
            result=model.checkUser(username,password)
            print(result)
            res = make_response(redirect('/'))
            res.set_cookie('name', username, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            return res

        except:
            return redirect('/register')




@app.route("/add",methods=['POST','GET'])
def add():
    if request.method=='GET':

        return render_template('add.html')
    elif request.method=='POST':

        user = request.cookies.get('name')
        userid = model.lookUser(user)

        name = request.form['name']
        desc = request.form['content']
        print(name, desc, userid[0])
        try:
            model.inserData(name,desc,userid[0])
            return redirect('/detail')


        except:
            return redirect('/add')

@app.route("/quit")
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie("name")
    return res


@app.route("/detail",methods=['POST','GET'])
def detail():
    if request.method=='GET':
        username = request.cookies.get('name')
        userid = model.lookUser(username)
        res=model.checkData(userid[0])
        # print('xxxxxxxxxxxxxxxxxxxxx',res)
        return render_template('detail.html',descinfo=res)
    elif request.method=='POST':
        #获取用户名
        username = request.cookies.get('name')
        userid = model.lookUser(username)
        res = model.checkData(userid[0])
        print('xxxxxxxxxxxxxxxxxxxxxxxx',res)
        try:
            id = request.form['id']
            id=int(id)
            for asd in res:
                a = asd[0]
                # print('111111111111111111',asd[0])
                # print(type(a))
                # print(type(id))
                if id == a:
                    # print('2222222222222222',a)
                    model.delData(id)
                    return redirect('/detail')
            else:
                return redirect('/detail1')

        except:
            return redirect('/detail')


@app.route("/detail1",methods=['POST','GET'])
def detail1():
    if request.method=='GET':
        username = request.cookies.get('name')
        userid = model.lookUser(username)
        res = model.checkData(userid[0])
        # print('xxxxxxxxxxxxxxxxxxxxx',res)
        return render_template('detail1.html',descinfo=res)
    elif request.method=='POST':
        try:
            id = request.form['id']
            id=int(id)
            id1 = request.form['id1']
            id2 = request.form['id2']

            username = request.cookies.get('name')
            userid = model.lookUser(username)
            res = model.checkData(userid[0])


            for asd in res:
                a=asd[0]
                print('ssssssss',a)
                if id==a:
                    model.ameData(id,id1)
                    model.ameData1(id,id2)
                    return redirect('/detail1')
            else:
                return redirect('/detail1')
        except:
            return redirect('/detail1')

if __name__=='__main__':
    app.run(host='192.168.12.133',port=8849)
