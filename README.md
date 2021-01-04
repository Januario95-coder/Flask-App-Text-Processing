Flask by Example
Blog Posts
This is the repo for the Real Python blog series, Flask by Example -

Part One: Set up a local development environment and then deploy both a staging and a production environment on Heroku.
Part Two: Set up a PostgreSQL database along with SQLAlchemy and Alembic to handle migrations.
Part Three: Add in the back-end logic to scrape and then process the word counts from a webpage using the requests, BeautifulSoup, and Natural Language Toolkit (NLTK) libraries.
Part Four: Implement a Redis task queue to handle the text processing.
Part Five: Set up Angular on the front-end to continuously poll the back-end to see if the request is done processing.
Part Six: Push to the staging server on Heroku - setting up Redis and detailing how to run two processes (web and worker) on a single Dyno.
Part Seven: Update the front-end to make it more user-friendly.
Part Eight: Add the D3 library into the mix to graph a frequency distribution and histogram.
Check out http://realpython.com

Quick Start
First Steps
$ pyvenv-3.5 env
$ source env/bin/activate
$ pip install -r requirements.txt
Set up Migrations
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
Run
Run each in a different terminal window...

# redis
$ redis server

# worker process
$ python worker.py

# the app
$ python app.py