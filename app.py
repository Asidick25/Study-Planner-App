# Importing the Flask class from the module
from flask import Flask 

# Initialise the application
app = Flask(__name__)

if __name__ == "__main__":
    # Starting the application in debug mode to identify errors
    app.run(debug = True)