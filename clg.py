from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/college')
def college_page():
    items=[{
        'college':"IITB", 'placement':20000
    }]
    return render_template('college.html', items=items)
