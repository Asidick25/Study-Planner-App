# Project Overview

## Project Introduction
This project is a user-friendly web-based application that is designed to help NCH Apprentices organise their yearly schedules effectively. The app allows the users to upload their timetables provided to them in the induction, visualise all the deadlines on an interactive calendar, and manage their time effectively. With an interactive, accessible and modern design, the study planner app aims to enhance the productivity of apprentices and reduce the stress associated in planning multiple deadlines. 

Key features include:
- Timetable upload feature where users can upload their timetables as a `.csv` or `.xlsx` file.
- An interactive monthly calendar that displays all the tasks and deadlines.
- Task Addition Feature to add new tasks directly into the calendars.
- Naviagtion for viewing deadlines across various months and years.

The app will allow students to balance their apprenticeship requirements and assignments together with work and personal commitments.

## The Project Roadmap
![image](https://github.com/user-attachments/assets/7fce0552-001b-406b-a5ae-07b62b792e23)

## Requirements
### Functional Requirements 
1. User Interface (UI)
   - Timetable Upload:
     Users should have an input field to be able to upload their timetable files as CSV or XLSX.
   - File Validation:
     Users receive information about the invalid file types during the upload.
   - Calendar Display:
     A calendar view should be displayed with the tasks and their corresponding deadlines.
   - Task Management:
     The ability for the users to add, edit or delete tasks from the calendar using the 'SAVE' or 'CANCEL' buttons.
   - Monthly Navigation:
     Users have the ability to navigate between months using the 'Previous' and 'Next' buttons at the top of the calendar.

2. Timetable Data
   - File Processing:
     Retrival of information like the deadlines and dates from the uploaded timetables.
   - Dynamic Updates:
     Users are able to update the tasks without refreshing the page.

3. Validation
   - File Validation:
     Ensure the uploaded files have a specific format and columns.

4. Error Handling
   - Upload Errors:
     Display of user-friendly messages to the upload of unsupported file formats.

### Non-functional Requirements
1. Performance
   - The calendar naviagtion between the months and task additions should load up between 1-2 seconds.
   - The app has the ability to handle multiple uploads without a delay.
  
2. Responsive Design
   - Ensure the app works smoothly on desktops, tablets and mobile devices.
  
3. Accessibility
   - Ensure screen reader compatibilty and a accessible colour scheme for visually impaired users
  
4. Security
   - Prevent the upload of malicious scripts by santising the user inputs.

## User Stories
User stories are ways of defining the features of the app from the perspective of the end-user. As they help to make the development user-centered, I made a few user stories based on the interaction with stakeholders. They are as below:
1. **Uploading Timetable:**

   As a student,

   I want to upload my timetable on the app

   So that I can track and visualise all my deadlines.

3. **Viewing tasks on calendar:**
   
   As a student,

   I want to view all my deadlines and tasks on a calendar

   So that my schedule can be managed more effectively.

5. **Adding new tasks**:
   
   As a student,

   I want to be able to add new tasks to the calendar

   So that my schedule can be updated without re-uploading the whole timetable.
   
## Stakeholders
![image](https://github.com/user-attachments/assets/ace522bd-c6da-4951-b447-9704a6c46034)

## Risks
To access the potential risks that may come up in the process, I made the risk matrix below that allows me to make a list of all potential risks and think of strategies to mitigate them.
![image](https://github.com/user-attachments/assets/eaa9410b-cb46-479b-8eda-f140acf4b0f0)

# Project Management

## Project Management Tools
To ensure the effective planning of the app, the following tools were being used during development:

1. GitHub Projects:
   GitHub was the central tool used for organising, tracking, and managing tasks and code changes. GitHub projects were very useful in structuring and monitoring the project workflow.
   To organise tasks, I made use of a KanBan Board with 5 main sections:

   - To-do:
     Tasks that have been written but face blockers before they can be started.
     This allowed me to capture all ideas and features, without the need to work on them immediately.

   - In Progress:
     Tasks that are refined, unblocked and ready to be started.
     They have clear descriptions and ensure smooth development.

   - Blocked:
     Tasks that have partially been left due to bugs and are awaiting input to be resolved.

   - Review:
     Tasks that have been completed but require a review for any changes.
     This ensures the quality of code through code reviews and testing.

   - Done:
     These are tasks that are complete and have been merged into the master branch.
     It provides help with progress tracking.
     
     ![image](https://github.com/user-attachments/assets/c846265d-8369-4d2c-a8a1-bfce04cd5d49)


   The issues were created for specific features, bugs, tests and enhancements. Each issue was labelled accordingly. Some of them are as below:
   - Bug: Issues that involve unexpected errors or incorrect functionality.
   - Enhancement: For improvements of existing features.

   The issues were managed directly through commits, ensuring tracibility between development progress and resolution.
   
1. VS Code
   VS Code served as the primary Integrated Development Environment (IDE) for writing, debugging and testing code. Key features that were used in development were:

   - Git Integration: Direct intergration between GitHub and VS Code that allowed to commit, push and pull changes easily.
   - Live Server: Provided a real-time preview of the app during development.
     

## Project Management Constraints

The limited time contraisnts of this project was a huge factor that affected the organisation and management of this project. Due to the tight timeline, I avoided the use of formal sprints and agile ceremonies which would only introduce extra effort to the project without any impact to the efficiency.

Instead, I made use of the Kanban methodology for project management. This allowed me to visualise tasks and priorities with no additional coordination.

Constraints:
- Time: With the limited time for development and testing, I focused on delivering the minimal viable product with the basic functionality. A lot needs to be done to improve the usability and quality of the app.
- Solo-Development: As a solo-developer, I was responsible for the development, testing and project management which led to the prioritisation of simple tasks.

## Project Organisation

### Labels
To manage the project, I made use of GitHub labels to categorise and prioritise tasks. These labels were applied to the issues and allowed me to therefore organise the project based on its nature, urgency and complexity of tasks.

The labels were created manually to suit the needs of the project. They provided a quick overview of the tasks, making it easier to filter the issues. Some labels were as below:
- Priority: `High`. `Medium` and `Low` to rank the issues based on their importance.
- Type: `Bug`, `Feature`, `Enhancement`, `UI/UX` and `Documentation`.
- Status: `In Progress`, `Blocked`, `Ready for Review`, `To-do` and `Done`.

The labels were flexible, allowing me to change them and add new ones as the project progressed. If the project was to be reviwed by someone, the labels would be helpful in understanding the project quickly.

![image](https://github.com/user-attachments/assets/03e64cab-ab33-4f5a-ab39-c98af258eb05)


### Priority
I made use of a priority-based labelling to organise the urgency of tasks. The categories were as below:
- High Priority: Tasks critical to the functionality of the app. They were addressed first to ensure we have a MVP at the end of the timeline.
- Medium Priority: Tasks that are important but not immediately critical. They were mainly for the enhancement of the app's visual appeal and usability.
- Low Priority: Tasks that were non-essential such as those that required minor adjustments.
  
This type of labelling made it easier to manage the project by working through the tasks in order of importance.

### Ticket Formatting
To ensure that the issues were consistent, I made use of a ticket template which was tilored to the various tasks. The template was as below:
- Title: What the issue was about
- Description: A brief description of the issue
- Objectives: A list of all the things that need to be achieved in this issue

This format reduced the time needed to create a ticket and ensures that all important information is captured.

![image](https://github.com/user-attachments/assets/ef4262a9-ea65-4b4c-977b-69d9fe840c57)


# Project Planning

## Project Design
The initial step in planning an application's front-end design, involved the use of Figma to create wireframes of potentiall design layouts. It is essential in visualising the overall structure of the app and planning its usability before the implementation.
I started by the identification of the key user actions in the app which were being outlined in the requirements. I then created an activity digaram to visually represent the sequence of user interactions with the app. 

The diagram included:
1. Timetable Upload: Users upload `.csv` or `.xlsx` files.
2. File Validation: The system identifies the uplaoded files and the correct format.
3. Calendar Navigation: After uploading the timetable, the users are able to view deadlines by month and year on the calendar.
4. Task Management: Users can add or modify tasks in the calendar.
5. Error Handling: Users are displayed error messages on incorrect inputs.

The design then priortised a visually clean and user-friendly interface. Some key considerations were:
- Ease of Navigation: The users should be able to easily upload their timetables and navigate between the different calendar views.
- Task Visibility: Deadlines and tasks should be clearly visible and colour coded for the ease of tracking.
- Responsiveness: A responsive interface that adapts across devices.

Figma(https://www.figma.com/proto/b2gdhZnRpqU3K6B3S59aqg/Study-Planner-App?node-id=3-3&t=tcjOHCxKPgNLwtU9-1) was used to create mock-ups which helped to plan the following:
- The **homepage**, with a clean layout for uplaods and year selection.
- The **calendar view**, ensuring the deadlines were easy to read and naviagte.
- **Task Management Tools**, allowing the users to add tasks.

![image](https://github.com/user-attachments/assets/4daffe93-8e55-47ce-a739-4fe6f7737944)

![image](https://github.com/user-attachments/assets/616c6a8c-5e9e-4aca-be41-cd6ee4fb0e3f)

![image](https://github.com/user-attachments/assets/2377e704-9840-480d-85b9-466f5d3e5035)


## Application Design

### Colour Scheme
A key consideration during the designing of the app, was accessibility through colour schemes to ensure the app was inclusive for users with colour blindness, visual impairments, or other disabilities. Studies show that around 4.5% of the global population has some form of colour blindness, which amounts to approximately 350 million people worldwide. Visually impaired users also struggle with poor contrast ratios, making it hard to interact with certain UI elements. 

For example, In 2019, LinkedIn received backlash for introducing dark mode that failed to meet the contrast ratio standards with user reporting difficulty in distinguishing text from the background.

I referred to Web Content Accessibility Standards (WCAG) to ensure that my app meets the accessbility standards. These were some things that I considered:
- High Contrast Ratios:
  The background gradients were subtle and ensured enough contrast with the text.
  Buttons were also dark green with hover effects for visual feedback.

- Task Deadlines:
  Cells with deadlines were filled in red to gain attention and hover text was used for additional feedback.

- Error Messages:
  Error messages were shown in red, with descriptive text for users with visual impairments.

### Error Handling
To ensure smooth user experience, error handling was carefully added into the app. The error messages were directly displayed on the screens for clarity and accessibility. 

For example:
= File Upload Errors: Clear messages being displayed when files in wrong format are being uploaded or when no file is selected.


### Final Design
The app has been designed with simplicity in mind, ensuring all critical functionality is easily accessible. Key screens include:

**Homepage**
- A clean layout with an upload option and a dropdown menu that appears upon the sucessful uplaod of the timetable.
- A central image of a laptop and a girl studying for a modern feel
- Clear text instructions as a guide.

**Calendar Page**
- A responsive calendar interface displaying deadlines.
- Navigation buttons for switching between months.


# Project Development

## Development Overview
After the planning and design stages, the development of the app started with the creation of a Flask web-based application. Flask was chosen due to its flexible and simple nature together with its ability to integrate Python with web interfaces. The app was built using modular development practice, where components of the app were developed, tested and debugged independently. 

Below is an outline of the project timeline with the main stages of development:
1. Project Initialisation:
   - Creation of a virtual environment to manage dependencies.
   - Initialisation of a GitHub repository and the set-up of feature branches.
   - Creation of a basic flask structure.
  
2. File Upload Development:
   - Developed a validation function for validating file types.
   - Developed file upload route using Flask.
   - Processed uploaded files using Pandas to extract tasks and deadlines.
  
3. Testing Setup:
   - Creation of test cases.
  
4. UI Development:
   - Designing of the homepage with user-friendly interface.
   - Creation of the calendar page to display tasks and deadlines efficiently.
   - Task addition feature to allow users to manually edit the calendar.

5. Calendar Logic
   - Developement of a logic to render tasks and deadlines.
   - Implemented the ability to navigate between months.

6. Error Handling
   - Display of clear, user-friendly messages for invalid inputs.
   - Improved accessibility of error messages by placing them near the errors.
  
7. End to end testing
   - Ensuring seamless integration between the back-end logic and the user interface.
   - Validation of the correct appearance of deadlines.
  
Some key development features:
1. Incremental Development: Each feature was developed in a seperate branch and merged into the main branch after passing code reviews.
2. Agile Approach: An interative approach was used to priortise critical features.
3. Accessibility Centric Design: The UI was designed with the W3C accessibility guidelines in mind.



# Test Driven Development
Test Driven development is an approach where tests are aimed to be written before implementing functionality and ensuring that the functionality is tested and validated during development. Whilst this wasn't fully done due to time constraints, tests were developed to validate the core functionality.

I started by setting up the `unittest` framework to test key components of the application. The focus was on the validation of:
- File uploads ensuring valid file types are accepted.
- Extraction of deadlines and tasks from the uploaded timetable.

However, I faced some challenges in the testing phase. One of them was the environment configuration where the `app` module could not be imported due to misconfigurations in the project structure. This made it hard to stimulate real world interactions.

In the future, I will make sure to adjust the current structure by separating the app logic in smaller, independent modules.


# Usability & Accessibility
In addition to the functional requirements, the app also focused on non-functional requirements such as:
- Responsive Design: The app working on both mobile phones and desktops.
- Performance: The app ensuring smooth user interactions with fast laod times.
- Accessibility: The app having accessibility features such as clear navigation and proper contrast ratios.

## Performance
To ensure the good performance of the application, I manually measured key aspects of performance such as page load times and responsiveness.

Performance Tests:
1. File Upload Speed: Varying sizes of `.csv` and `.xlsx` were used to enure that the uplaods are completed within 2 seconds.
2. Navigation Speed: Ensuring the transitions between the pages was smooth and quick.
   
## Accessibility
Accessibility was a major part of the development and whilst accessibility standards were followed and checked against the standards, some more improvements could have been made to improve accessibility.

For example:
- ARIA Attributes: These are roles and labels that could have added to all interactive elements to be read by screen readers.
- Keyboard Navigation: Focus indicators could have been added to buttons and links to ensure users can navigate through the app with the use of keyboards.

# Project Analysis and Reflection
The project proposal laid out several functional and non-functional requirements and compairing against those, the project still needs a bit of development. 

Reflection:

1. User Interface:
   - Timetable Upload:
     Requirement: Users are able to upload timetables in `.csv` or `.xlsx` format.
     Implementation: Achieved using a file upload field with validation in the back-end to prevent wrong file types.

   - Calendar Display:
     Requirement: An interactive calendar view displaying tasks and deadlines.
     Implementation: The calendar dynamically loads tasks. But the latter are not colour coded and properly formatted.

   - Task Management:
     Requirement: Users can add new tasks to the calendar.
     Implementation: Implemented the add task button that allows users to add details of their tasks but the tasks don't appear on the calendar yet.

2. Timetable Data
   - File Validation:
     Requirement: Validating file formats and timetable structure upon upload.
     Implementation: A validation function that ensures that only .csv and .xlsx files are processed.
     
   - Dynamic Task Updates:
     Requirement: Users are able to update tasks without re-loading timetable.
     Implementation: Feature not integrated yet.

3. Backend Logic
   - Calendar Rendering
     Requirement: Convert uploaded timetable into calendar.
     Implementation: Created a `make_calendar` function to structure deadlines by month and week.

    - Deadline Display:
      Requirement: Display the tasks on respective dates.
      Implementation: Integrated tasks directly into calendar cells. Distinct colors need to be implemented.

4. Non-functional Requirements
   - Responsive Design:
     Requirement: Ensure usability on various devices
     Implementation: Not fully implemented.
     
   - Performance:
     Requirement: Ensure calendar and task updates occur within 1–2 seconds.
     Implementation: Target achieved.

   - Accessibility:
     Requirement: Design for screen readers and visually impaired users.
     Implementation: Ensured contrast ratios meet WCAG 2.1 standards and colour scheme is accessible.

# Future Scope
With additional time some of the below could be integrated to improve its functionality, adding more value to users:

1. Machine Learning Integration 
- Smart Task Suggestions: ML models that analyse user data and suggest the optimal time for task completion.
- Deadline Conflict Detection: Use of predictive analytics to identify potential conflicts and suggestions to get through them.
- Priority Predictions: Automatic prioritisation of tasks based on their urgency and importance whilst taking deadlines in consideration.

2. Pomodoro Timer
- Integration of a Pomodoro timer to help users manage their study sessions efficiently.

3. Gamification Features
Achievement Badges: Rewarding users for completing tasks or effectively managing their schedules.


# References:
Colour Blind Awareness, 2023. Facts about Colour Blindness. Available at: https://www.colourblindawareness.org/ (Accessed 24 January 2025).
Flask, 2023. Testing Flask Applications. Available at: https://flask.palletsprojects.com/en/stable/testing/ (Accessed 24 January 2025).
Forbes, 2023. How the Pomodoro Technique Can Help Your Productivity. Available at: https://www.forbes.com/ (Accessed 24 January 2025).
W3C, 2023. Web Content Accessibility Guidelines (WCAG). Available at: https://www.w3.org/WAI/standards-guidelines/wcag/ (Accessed 24 January 2025).

