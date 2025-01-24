# Importing packages
import os
import pandas as pd
from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect, url_for,session


# Initialise the application
app = Flask(__name__)
app.secret_key = 'Key'

# Route of the app
@app.route('/')
def home():
    return "Welcome to the Study Planner App!"

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

## File Upload Route

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





### Calendar Displays

## Calendar function:
# Function to make calendar

def make_calendar(deadlines):
    """Function to generate a monthly calendar with tasks based on the deadlines in the calendar. 
    
    Arguments:
       deadlines (list of dictionary): A list of dictionary where each dictionary is for a deadline.
       They keys are: 'date' (string in ""YYY-MM-DD") and 'task' (string).
    
    Return:
       calendars (dict) : A dictionary where keys are (year,month) tuples and values are calendars for each month.
       Each calendar is a list of weeks.
       Each week is a list of days with the tasks.
    """
    
    from collections import defaultdict
    import calendar

    # Deadlines by month
    deadlines_by_month = defaultdict(list)

    # Iterating through the deadlines and extracting the date of each task
    for deadline in deadlines:
        task_date = deadline["date"]
        
        # Validating and converting the dates to a datetime.date object
        try:
            # Ensure the date is a string before converting
            if isinstance(task_date, str):
                task_date_obj = datetime.strptime(task_date, "%Y-%m-%d").date()
            elif isinstance(task_date, datetime):
                task_date_obj = task_date
            else:
                    # Skip if the date format is invalid
                continue
            
            # Grouping deadlines by month and appending the tasks to the corresponding list
            year_month = (task_date_obj.year, task_date_obj.month)
            deadlines_by_month[year_month].append({
                "date": task_date_obj,
                "task": deadline["task"]
            })
        
        except Exception as e:
            print(f"Skipping invalid date: {task_date} with error: {e}")
            continue
    
    # Initialising the monthly calendar
    calendars = {}
    for year_month, tasks in deadlines_by_month.items():
        year, month = year_month
        month_calendar = []  # Calendar for this month
        week = [{"date": None, "task": None} for _ in range(7)]

        # Determine the first and last days of the month and adjusting for transitions
        first_day = datetime(year, month, 1).date()
        if month < 12:
            last_day = datetime(year, month + 1, 1).date() - timedelta(days=1)
        else:  # Handle December separately
            last_day = datetime(year + 1, 1, 1).date() - timedelta(days=1)


        # Fill in the days of the month
        current_date = first_day
        while current_date <= last_day:
            day_index = current_date.weekday()  # Monday=0, Sunday=6

            # Find a task for the current date, if any
            task = next((d["task"] for d in tasks if d["date"] == current_date), None)
            week[day_index] = {"date": current_date.strftime("%Y-%m-%d"), "task": task}

            # If the week is complete, add it to the calendar
            if day_index == 6:
                month_calendar.append(week)
                week = [{"date": None, "task": None} for _ in range(7)]

            current_date += timedelta(days=1)

        # Add the remaining week if it contains any dates
        if any(day["date"] for day in week):
            month_calendar.append(week)

        # Add the month's calendar to the result
        calendars[year_month] = month_calendar

    return(calendars)


## Calendar Route:

@app.route('/calendar')
def calendar():
    # Get the selected year
    sel_year = request.args.get('year')
    sel_month = request.args.get('month')

    # Get deadlines from the session
    deadlines = session.get('deadlines', [])

    # Filter deadlines for the selected year
    sel_year_deadlines = [
        {"date": deadline["date"], "task": deadline["task"]}
        for deadline in deadlines
        if deadline["year"] == sel_year
    ]

    if not sel_year_deadlines:
        return render_template('calendar.html', deadlines=[], error="No tasks for the selected year.")

    # Generate the calendar grouped by month using the make_calendar function
    deadlines_by_month = make_calendar(sel_year_deadlines)

    # Get the calendar for the selected month
    if sel_month:
        try:
            sel_month = int(sel_month)
        except:
            sel_month = None

        selected_calendar = deadlines_by_month.get((int(sel_year), sel_month), [])
    else:
        # Default to the first month with tasks if no month is specified
        first_month = min(deadlines_by_month.keys(), default=None)
        if first_month:
            sel_year, sel_month = first_month
            selected_calendar = deadlines_by_month[first_month]
        else:
            sel_year = None
            sel_month = None
            selected_calendar = []

    if not selected_calendar:
        # Create a blank calendar for the selected month
        selected_calendar = [[]]

    # Make navigation links
    months_with_data = sorted(deadlines_by_month.keys())

    try:
        current_index = months_with_data.index((sel_year, sel_month))
        prev_month = months_with_data[current_index - 1] if current_index > 0 else None
        next_month = months_with_data[current_index + 1] if current_index < len(months_with_data) - 1 else None
    except ValueError:
        prev_month, next_month = None, None


    return render_template(
        'calendar.html',
        deadlines=selected_calendar,
        current_month=sel_month,
        current_year=sel_year,
        prev_month=prev_month,
        next_month=next_month,
    )


if __name__ == "__main__":
    # Starting the application in debug mode to identify errors
    app.run(debug = True)