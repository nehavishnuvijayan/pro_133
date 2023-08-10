# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home1():

    return render_template('index.html' , name = "neha", age = "17")
# define the route to father webpage
@app.route("/dad")
def home2():

    return render_template('father.html' , name = "vishnu" , age = "47")

# define the route to mother webpage
@app.route("/mom")
def home3():

    return render_template('mother.html' , name = "divya" , age = "42")

# define the route to friends webpage
@app.route("/dude")
def home4():

    return render_template('friend.html' , name = "shreya" , age = "17")

# add other routes, if you want




# run the file

app.run(debug=True)
