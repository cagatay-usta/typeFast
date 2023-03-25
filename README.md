# typeFast
#### Video Demo:  <URL HERE>
#### Description:

typeFast is a web app to practice typing different naming conventions such as camelCase, snake_case and kebab-case.

typeFast is developed as the final project for the CS50 course, with the timeframe of 14 days.

## Languages and Frameworks

I used html, css, javaScript for the front-end with bootstrap, and python, flask and sqlite3 for the back-end.

## Design and Prototyping

Starting with a simple idea, I used a simple text file to brainstorm and note down all my ideas.
Then I picked the ideas and features from that large list and scored them according to my knowledge and skill level,
time needed for implementation (the timeframe is 14 days for the project), and if they would play nice with other features 
or would they require fundamental changes like changing my frameworks. 

In the end, I decided to start with a working prototype which is highly modular and scalable so that in case if any part of the development
process takes longer than expected, I would have a working product at the end of the 14 day period, and if completed before then,
I could easily implement more features to it.

To start, I created a project on GitHub and my first todo list was this:

-	Design the layout
-   Design the homepage
-	Store words
-	Design the word generator algorithm
-	Design the WPM algorithm
-	Design the leaderboard
-	Create the leaderboard database

Creating a project and a todo list helped me with ordering priorities and a roadmap to work on without getting stuck on deciding what to do next.
I also used the roadmap view feature on GitHub to eyeball the time needed for each and measure how fast they are completed.

### Layout and Aesthetics Design

I utilized bootstrap and kept everything simple with a black and white theme. Minimalistic design stemmed from both the time constraint 
and the spirit of the app as its design philosophy is to get the user as fast as possible to the core function of the app, that is to practice 
typing without any distractions or unrelated features.

## Algorithms

### Word Generator Algorithm

First task in the word generator algorithm was to prepare the base words to be used later in combination with others to create "cased" words.
I searched for top 500 common words in English and downloaded an Excel file containing the words and other additional info like frequency, order and etc. As I only needed the words, I saved the file as .csv and created a short python app to create a new file only with the data I needed. This the few lines of python that enabled me to extract the words:
```python
import csv

database = []
with open("english-word-list-total.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        database.append(row)

newDatabase = []
for row in database:
    newDatabase.append(row['word'])

with open('500-words', 'w', newline='') as newFile:
    writer = csv.writer(newFile)
    for row in newDatabase:
        writer.writerow([row])

```

I then progressed to created a new python document to work on utility functions like the word generator and the wpm (words per minute) calculator. They are kept in a different .py as I wanted to keep the readability of the app.py clear and to be able to test the functions first in a "vacuum".
Word generator algorithm is really simple as it simply takes two words from the csv file and concatenate them depending on the case. When designing it I kept in mind that if in future versions I wanted to add more case options or other words to pick from, I could do it without completely throwing out the algorithm but instead add a few parameters or a new condition and it will be ready.

### WPM Calculator

For wpm calculator, I used the popular convention of "any 5 characters typed without a typo counts as a word" to reduce the chance factor of getting too many longer or shorter words. To check the correct spelling, I placed a hidden input in the html form where the value is the same to the words generated and presented to user, and later compared the user input and the words generated in python.

### Timer

Although seemed simple, displaying a timer and moreover using it the value of it in the back-end with python to calculate wpm has been a challange and was an example of an unexpected bottleneck regarding time management when calculating the total time needed. In the end, I gained a lot of new knowledge in JavaScript and designed a simple countdown timer, also I placed another hidden input into the form that submitted both the user-typed words and the remaining time (updated using JS).

## Leaderboard and Database

I used a simple leaderboard layout consisting of WPM and the time of entry of the top ten wpm records. And thus the sqlite3 database is also short and concise, consisting only of:

```SQL

CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY,
    wpm REAL,
    record_time TEXT
);

```

I kept all my sql query logs in queries.sql to avoid typos and backtracking when used later. 
After setting up the database, both inserting new entries and displaying them in the leaderboard was easy. 

### Future Improvements
Although I am content with the current state of it for the final project, there are some features I had in my mind when desinging that couldn't make it into the final product due to time constraints. However, I specifically designed the whole project with the intention of adding more features later, thus in a modular design. Here are some ideas of new features and improvements:
- Using AJAX to display current WPM
- User login to see individual WPM records
- More case convention types
- Individual stats displaying how WPM progressed over time
- More base texts to choose from or that users can upload their own words to generate cased words
- Users can change the time length

## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).