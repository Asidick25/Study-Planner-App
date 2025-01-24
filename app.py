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

# Setting route for uploading the file with both GET(to load the page) and POST(to handle the uploads) HTTP methods
@app.route('/', methods = ['GET', 'POST'])
def file_upload():
    """Function that handles file uploads and processing.
    
    Methods: ['GET','POST']

    Inputs: File uploaded by the user

    Return: Renders the index.html file with the extracted years and error messages.
    """
    
    # Variable to hold the unique years extracted from the timetable
    years = None

    # Variable to store error messages to be displayed to the user
    error = None

    # The use of the POST method when users submit a file.
    if request.method == 'POST':
        # Ensuring of the file exists in the uplaoded data
        if 'file' not in request.files:
            # If the file doesn't exist, an error message is displayed
            return render_template('index.html', error="No file selected. Please try again.")
        
        # The uploaded file is retrived
        file = request.files['file']

        # Checking if a file is selected.
        if file.filename == '':
            return render_template('index.html', error="No file selected. Choose a file please.")
        
        # Validating the file type by the use of the allowed_file_check() function to make sure it has a valid extension.
        if allowed_file_check(file.filename):
            
            # Checking if the upload folder exists. If not, a folder is created.
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])


            # Sanitize the filename to avoid issues using Flask's secure_filename function
            from werkzeug.utils import secure_filename
            safe_filename = secure_filename(file.filename)

            # Saving the file in the upload folder
            filepath = (os.path.join(app.config['UPLOAD_FOLDER'], safe_filename))
            file.save(filepath)

            # Processing the file into a Pandas dataframe and extracting the years
            try:
                if file.filename.endswith('.csv'):
                    data=pd.read_csv(filepath, header=1)
                elif file.filename.endswith('.xlsx'):
                    data=pd.read_excel(filepath, header=1)

                # Taking out the unique years from the timetable
                years = sorted(data['YEAR'].dropna().unique())

                # Storing deadlines in the session
                # Extract deadlines and store as dictionaries in session
                session['deadlines'] = []
                for _, row in data.iterrows():
                    try:
                        # Converting the date column to ensure consistent format
                        date_str = row["END DATE"]
                        # Converts to "YYYY-MM-DD"
                        date_obj = pd.to_datetime(date_str).strftime("%Y-%m-%d")
                        # Appending the (YEAR, END DATE, PROGRAMME) to the deadlines list
                        session['deadlines'].append({
                            "year": str(row["YEAR"]),
                            "date": date_obj,
                            "task": row["PROGRAMME"]  # Adjust column name as per your file
                        })

                    except Exception as e:
                        # Handle individual row errors and if they have errors, skip them
                        continue

            except Exception as e:
                        return render_template('index.html', error = f"Error processing file: {e}" )
            
            
            return render_template('index.html', years=years)
        
        else:
            return render_template('index.html', error="Invalid file type. Only .csv and .xlsx files are accepted.")


    # When the file is successfully processed, the html page is rendered with the extracted years
    return render_template('index.html', years=years)




if __name__ == "__main__":
    # Starting the application in debug mode to identify errors
    app.run(debug = True)