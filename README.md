# TrackMyHabits by CosmicWhiskers, 2024
 The Habit Tracker offers a straightforward, user-friendly tool compatible with any platform that supports Python 3. To keep the application lightweight and widely accessible, it’s designed to run within a command-line interface, making it usable even on systems without a graphical user interface.

Users can track their habits effortlessly by creating, managing and viewing habits in an organized layout. Doing so, helps them monitor their progress. Analytics features provide insights, such as number of habits, habit streaks, top-performing and more.

This habit-tracker is being created in the context of a continuing education course (Data Analyst - Python) for the module "Object-Oriented and Functional Programming with Python (DLBDSOOFPP01)".

# Quick start
This project requires python 3.12.7+ and pip installed.

## Installation
Clone this repository:

`git clone https://github.com/CosmicWhiskers/habit-tracker.git`

If you choose to install this in a virtual environment: 
`python -m venv venv`

To activate the enviornment:
`.\venv\Scripts\activate`

Install requirements and dependencies
`pip install -r requirements.txt`

## Running
To start the application:
`python main.py`

## Testing
run `pytest`

# Diagrams/Concept

## UML/class Diagram

### Database
![Alt text](diagrams/classes.png?raw=true "Database")

### Class Diagram
![Alt text](diagrams/classes.png?raw=true "Class Diagram")
### Userflow 
![Alt text](diagrams/userflow.png?raw=true "Userflow Diagram")



## User interface
### Welcome Screen
Short notice indicating a successful program start
### Main Menu
The Main Menu works as a hub for users to manage their habits. Here users can choose between managing their habits, checking off Active Habits, see statistics or, 
just end the program altogether
### Habits
In the Habit screen users can choose to create a new habit, edit an existing habit, or delete them
#### New Habit
The New Habit screen enables the user to create a new habit. The user can either choose from 5 pre-existing habits, or create a completely new one. 
In addition, users can set the type (daily, weekly) and duedate of the habit.
#### Edit Habit
In the Edit Habit screen users can change certain attributes of an active habit to adjust them to the personal needs of the user.
Those attributes can be name, type (daily weekly), or duedate.
#### Delete Habit
The Delete Habit Screen shows all habits currently existing. By selecting a habit the habit will be removed and permanently deleted. 
### Check Active Habits 
In the Check Active Habits screen users can check off the habit(s) they completed
### Statistics
The Statistics screen shows information about 
+ the number of active habits, 
+ the longest run streak of all active habits, or for a specific one 
+ habits with the same periodicity
### End Program
Terminates and exits program.

## Test/Sample data


# License