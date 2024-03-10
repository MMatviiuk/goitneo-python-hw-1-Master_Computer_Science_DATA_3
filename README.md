1. Implementation of a function to display a list of colleagues who need to be greeted with a birthday this week.

2. Write a bot assistant that can recognize commands entered from the keyboard and respond accordingly to the entered command.

General acceptance criteria

Tasks are executed in exact accordance with the technical description (recommendations for execution and evaluation criteria). There are no errors or warnings in the console when starting the bot. Variable and function names are clear and descriptive. The code is formatted and complies with the PEP8 standard. Evaluation format Score from 0 to 100

Brief technical task

Task 1: In the first stage, you need to implement a function for displaying a list of colleagues who need to be greeted with a birthday this week.

You have a list of dictionaries called users, each dictionary must have keys name and birthday. This structure represents a model of a user list with their names and birthdays. Where name is a string with the user's name, and birthday is a datetime object that contains the user's birthday.

Your task is to write a function get_birthdays_per_week, which takes a list of users as input and prints to the console (using print) a list of users who need to be greeted for their birthdays next week. Users whose birthday falls on weekends should be greeted on Monday. The function displays users with birthdays for the week ahead from the current day. The week starts on Monday.

Task 2: Write a console assistant bot that will recognize commands entered from the keyboard and respond accordingly to the entered command.

THE ASSISTANT BOT SHOULD BE A PROTOTYPE FOR THE APPLICATION ASSISTANT WE WILL DEVELOP IN THE FOLLOWING HOME TASKS. THE ASSISTANT APPLICATION IN THE FIRST APPROACH SHOULD BE ABLE TO WORK WITH THE CONTACT BOOK AND CALENDAR.

In this homework, we will focus on the interface of the bot itself. The simplest and most convenient interface for bot development at the initial stage is a CLI (Command Line Interface) console application. CLI is quite easy to implement. Any CLI consists of three main elements:

Command parser. The part responsible for parsing the strings entered by the user, extracting key words and command modifiers from the string.
Command handler functions - a set of functions, also called handlers, responsible for directly executing commands.
Request-response loop. This part of the application is responsible for receiving data from the user and returning responses from the handler function.
In the first stage, our assistant bot should be able to store a name and phone number, find a phone number by name, change the recorded phone number, and output all stored records. To implement such a simple logic, we will use a dictionary. We will store the user's name as the key and the phone number as the value in the dictionary.

You can leave error handling at your discretion in this homework, as in the next homework, we will add error handling through decorators.

Evaluation Criteria:

The bot should be in an infinite loop, waiting for user commands.

The bot terminates its operation if it encounters the words: "close" or "exit".

The bot is case-insensitive to the entered commands.

The bot accepts commands:

"hello", and responds in the console with the message "How can I help you?"

"add username phone". With this command, the bot stores a new contact in memory, for example, in a dictionary. The user enters the username name and phone number phone, separated by a space.

"change username phone". With this command, the bot stores a new phone number phone in memory for the username contact, which already exists in the notebook.

"phone username" With this command, the bot outputs the phone number to the console for the specified contact username.

"all". With this command, the bot outputs all saved contacts with phone numbers to the console.

"close", "exit" with any of these commands, the bot ends its operation after displaying the message "Goodbye!" to the console and terminates its execution.

The logic of commands is implemented in separate functions, and these functions take one or more strings as input and return a string.

All interaction logic with the user is implemented in the main function, all print and input occur only there.
