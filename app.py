from flask import Flask, request, render_template
import sqlite3
import csv
from helper_functions import word_generator, wpm_calculator

# global variables for the default parameters of the word generator
NUMBER_OF_WORDS = 50
DEFAULT_CASE = 'camelCase'


app = Flask(__name__)


# connect to sqlite database
con = sqlite3.connect("typefast.db", check_same_thread=False)
db = con.cursor()


# store the words to memory from the csv
with open("500-words.csv") as file:
    words = [word.rstrip() for word in file]


# main route 
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        casedWords = word_generator(words, DEFAULT_CASE, NUMBER_OF_WORDS)
        return render_template("index.html", casedWords=casedWords)
    
    if request.method == 'POST':

        if request.form.get('caseType'):
            casedWords = word_generator(words, request.form.get('caseType'), NUMBER_OF_WORDS)
            return render_template("index.html", casedWords=casedWords) 

        else:
            time = 60 - int(request.form.get('timeLeft'))
            wpm = wpm_calculator(request.form.get('shownWords'), request.form.get('typedText'), time)

            # connect to database to save the record
            con = sqlite3.connect("typefast.db", check_same_thread=False)
            db = con.cursor()
            db.execute("INSERT INTO leaderboard(record_time, wpm) VALUES(DATETIME('NOW'), ?)", [wpm])
            con.commit()
            con.close()

            return render_template("index.html", wpm=wpm)

    
@app.route("/leaderboard", methods=["GET", "POST"])
def leaderboard():
    if request.method == "GET":
        # connect to database to get the records
        con = sqlite3.connect("typefast.db", check_same_thread=False)
        db = con.cursor()
        db.execute("SELECT wpm, record_time FROM leaderboard ORDER BY wpm DESC LIMIT 10")
        records = db.fetchall()
        con.close()
        return render_template("leaderboard.html", records=records)


# close connection to database when done 
con.close()

