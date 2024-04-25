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
        return render_template('login.html',message="registration complete kindly login now") 
    else:
        return render_template('register.html',message='regsitration not done email already exist')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')
    response=dbo.search(email,password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='login unsuccessful try again')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')
    

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')
    


app.run(debug=True)

