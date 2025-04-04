"""from flask import Flask

app = Flask(__name__)

@app.route("/") #go to the home page
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>' 
            '<p>This is a paragraph </p>' 
            '<img src =https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGR2NGpnMm4yZG0xOXh4aW1zZDN6NThld2xmYnJ4OXdvejF4MWlicyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/yFQ0ywscgobJK/giphy.gif>')

@app.route("/bye") #go to the home page
def bye():
    return "<p>Bye</p>"

# @app.route("/username/<path:name>") #go to the home page
@app.route("/username/<name>/<int:number>") #go to the home page
def greet(name,number):
    return f"<p>Hello there {name} you are {number} years old</p>"

if __name__ == "__main__":
    app.run(debug=True) """

from flask import Flask

app = Flask(__name__)

#Decorators to add a tag around text on web page.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


#Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


#Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
