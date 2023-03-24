from flask import Flask, request, render_template
import sqlite3
import csv
from helper_functions import word_generator

app = Flask(__name__)


# connect to sqlite database
con = sqlite3.connect("typefast.db")
db = con.cursor()


# store the words to memory from the csv
with open("500-words.csv") as file:
    words = [word.rstrip() for word in file]






# main route 
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == 'POST':
        return render_template("index.html") # when case selection submitted change the text to type
    
@app.route("/leaderboard", methods=["GET", "POST"])
def leaderboard():
    if request.method == "GET":
        return render_template("leaderboard.html")
    


# close connection to database when done 
con.close()

