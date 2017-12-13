from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li></ul><h1>Tomorrow's Movie</h1>"
    content += "<ul><li>" + get_random_movie() + "</li></ul>"

    return content

def get_random_movie():
	list = ["The Big Lebowski", "No Country for Old Men", "Fargo", "O Brother, Where Art Though", "Raising Arizona"]
	return random.choice(list)


app.run()
