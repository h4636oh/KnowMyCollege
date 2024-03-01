from flask import Flask, render_template,request
import pandas as pd


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

@app.route('/form',method=['GET','POST'])
def form():
    # this is method for taking a input 
    # just extend it for every parameater
    # for HTML part of this watch this Video https://www.youtube.com/watch?v=9MHYHgh4jYc
    
    if request.method== "POST":
        placement_pref = request.form["Placment"]
    else:
        return render_template("form.html")
    


#app runining with debug mode on 
if __name__=='__main__':
    app.run(debug=True)


# to activiate Virtual Env in Windows 
# .\env\Scripts\activate 

# to run the app use following command on windows 
# set FLASK_APP=app.py
# flask run
