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

### Algorithms and Database

TODO

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