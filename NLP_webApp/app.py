from flask import Flask, render_template, request, redirect, session
from db import Database

app = Flask(__name__) #__name__ parameter being crucial for Flask to set up
#the application properly, especially regarding routes, templates, 
#and static files.

dbo=Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get('user_ka_name')
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')

    response=dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message="registration complete kindly login now") #this is for opening login but
    #with extra info or message
    else:
        return render_template('register.html',message='regsitration not done email already exist')





app.run(debug=True)

