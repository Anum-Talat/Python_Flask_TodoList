import sqlite3
from flask import Flask, render_template, url_for, redirect, request
import my_functions
 
DATABASE = 'database.db'

app = Flask(__name__)




@app.route('/')
def home():
     my_functions.create_DB()
     test = my_functions.viewDB()
     return render_template('home.html', test = test)

@app.route('/add', methods = ["GET", "POST"])
def add():
     if request.method == "POST":
          title = request.form.get("title")
          my_functions.create_DB()
          my_functions.insertDB(title)
          return redirect(url_for("home"))
     elif request.method == "GET":
          return redirect(url_for("home"))
     

@app.route('/update/<int:id>')
def update_id(id):
     my_functions.create_DB()
     my_functions.updateTask(id)
     return redirect(url_for("home"))

@app.route('/delete/<int:id>')
def delete_id(id):
     my_functions.create_DB()
     my_functions.deleteTask(id)
     return redirect(url_for("home"))

@app.route('/clear')      # path to clear the task
def clear():
     my_functions.clear_all()
     return redirect(url_for("home"))
          
   

if __name__== '__main__':
    app.run(host= '0.0.0.0', port = 8000)

