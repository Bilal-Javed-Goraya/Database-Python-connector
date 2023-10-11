from flask import Flask
import mysql.connector

app=Flask(__name__)

@app.route('/')
def printHelloWorld():
    return '<h1>Hello World</h1>'

@app.route("/createStudent/<int:numbers>", methods =['POST'])
def createStudent(numbers):
    db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "dscsdcss",
    database = "mysql2"
     )
    
    cursor =db.cursor()
    query = f''' SELECT * FROM students LIMIT {numbers}'''
    cursor.execute(query)
    data =cursor.fetchall()
    return data