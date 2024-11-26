# main,py

# This is the main file for the Sunrise Alarm application.
# It uses the Flask web framework, which is a micro web framework
# written in Python. Flask is a great framework for small web
# applications, and is easy to learn and use.

# Import the Flask class from the flask module.
from flask import Flask

# Create an instance of the Flask class, passing in the name of
# the current module as the first argument. This is the standard
# way to create a Flask app.
app = Flask(__name__)

# The @app.route() decorator is used to associate a function with
# a specific URL. In this case, the home() function is associated
# with the root URL of the app, i.e. http://localhost:5000/.
@app.route('/')
def home():
    # The home() function is called when the user visits the root URL
    # of the app. It returns a simple string saying "Hello, Sunrise Alarm!".
    return "Hello, Sunrise Alarm!"

# @app.route('/location', methods=['POST']) 





if __name__ == '__main__':
    # The app.run() method is used to start the Flask development
    # server. The debug=True argument means that the server will
    # automatically reload if any changes are made to the code.
    app.run(debug=True)
