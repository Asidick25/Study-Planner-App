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

## Application Design

### Colour Scheme
### Error Handling
### Final Design

# Project Development

## Development Overview

# Test Driven Development

# Usability & Accessibility

## Performance
## Accessibility


# Project Analysis and Reflection

# Final Product and Visuals

# Future Scope
