# Importing packages
import os
import pandas as pd
from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect, url_for,session


# Initialise the application
app = Flask(__name__)
app.secret_key = 'Key'


### File Uploads

## File Validation

# Setting the upload folder for the timetables - a constant
# The path of the upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# Configures the flask application to use the specified folder to save all uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# The types of file extensions allowed for the uploads
ALLOWED_EXTEN = {'csv', 'xlsx'}

# Checking for the correct extensions:
def allowed_file_check(filename):
    """Function to check if a given file has an allowed extension.
    
    Arguments:
         filename (str): The name of the file check.

    Return:
         boolean: True if the file has an allowed extension, False otherwise.
    """
    
    # If filename has a '.'
    # If filename has a allowed extension
    if '.' not in filename:
        return False
    # Extracting the file extension by spilitting the filename at the '.'    
    extension = (filename.split('.')[-1]).lower()
    # Checking if the extracted extension is in the allowed extensions
    return extension in ALLOWED_EXTEN







if __name__ == "__main__":
    # Starting the application in debug mode to identify errors
    app.run(debug = True)