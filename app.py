from flask import Flask, render_template, url_for, redirect, request
from my_functions import *

app = Flask(__name__)


@app.route('/')
def home():
     create_DB()
     test = viewDB()
     return render_template('home.html', test = test)

@app.route('/add', methods = ["GET", "POST"])
def add():
     if request.method == "POST":
          title = request.form.get("title")
          create_DB()
          insertDB(title)
          return redirect(url_for("home"))
     elif request.method == "GET":
          return redirect(url_for("home"))
     

@app.route('/update/<int:id>')
def update_id(id):
     create_DB()
     updateTask(id)
     return redirect(url_for("home"))

@app.route('/delete/<int:id>')
def delete_id(id):
     create_DB()
     deleteTask(id)
     return redirect(url_for("home"))
@app.route('/clear')
def clear():
     clear_all()
     return redirect(url_for("home"))
          
   

if __name__== '__main__':
    app.run(host= '0.0.0.0', port = 8000, debug=True)

