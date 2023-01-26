from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'honey':'346','shehulk':'3012','prajwal':'2010'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    username=request.form['username']
    pwd=request.form['password']
    if username not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[username]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=username)

if __name__ == '__main__':
    app.run()