"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<br>Go to the 
    <a href="/hello">Hello Page</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="compliments">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
            <option value="Neato">Neato</option
            <option value="fabtabulous">fabtabulous</option>
            <option value="woza">Woza</option>
            <option value="oh-so-not-meh">Oh-so-not-meh</option>
          </select>
          <input type="submit" value="Submit">
        </form>

      <form action="/diss">
        What's your name? <input type="text" name="person">
          <select name="insults">
            <option value="not_awesome">Not Awesome</option>
            <option value="not_terrific">Not Terrific</option>
            <option value="not_fantastic">Not Fantastic</option>
            <option value="not_neato">Not Neato</option
            <option value="not_fabtabulous">Not fabtabulous</option>
            <option value="woza">not_woza</option>
            <option value="not_oh-so-not-meh">Not Oh-so-not-meh</option>
          </select>
        <input type="submit" value="Submit">
    </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")
    #compliment = choice(AWESOMENESS)
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def say_insults():

    player = request.args.get("person")

    insult = request.args.get("insults")
    #compliment = choice(AWESOMENESS)
    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """.format(player=player, insult=insult)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
