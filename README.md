# Higher/Lower Game

[Visit live website](https://high-low-cipp3.herokuapp.com/)

![Mockup image](docs/home_page.png)

## About

This is a command-line version of the classic Higher/Lower Game.

The purpose of the game is to guess the higher value, in this case the country population, and have a winning streak as high as possible witch counts as your score.

This particular version of the game gives you the ability to create an account and have your highest score stored.


## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Play a fun and easy game
- Test your knowledge of geography
- Be able to log in to an existing account

### Site Owner Goals

- Create a game that is easy and clear to user
- Ensure that users understand the purpose of the game
- Create a game that gives feedback to the user whilst playing

## User Experience

### Target Audience

There is no specific audience of this game.

### User Requirements and Expectations

- A simple, error-free game
- Straightforward navigation
- Game personalisation by entering players' names
- Feedback on game result

### User Manual

<details><summary>Click here to view instructions</summary>

    #### Main Menu
    On the main menu, users are presented with an ASCII art rendering of the name 'Higher/Lower'. Below the graphic the user is greet with a welcome message and asked if he is a returning user. The user can answer the question by typing "y" for yes or "n" for no. If anything else is typed, it will be asked to try again

    At any point of the game, if the user inputs somethig which do not correspond to the suggested options then they will be prompt to try again.

    #### New account
    If the user answer with no to the first question, then he will be asked to create a new account by entering a username and a passcode

    #### Log-in
    If user answer with yes to the "Are you a returning user?" question, then he must provide an existing username and a corresponding passcode.

    #### Play
    After the account creation or after a successful log in, the game starts.
    The question is printed to the terminal and the user must answer again with yes or no. This repeats until a wrong answer is given. Then the score is printed together with both countries populations.
    The option to replay is given to the user. If he chooses not to play again, then the top 5 scores are printed to the terminal

</details>


## User Stories

### Users

1. I want to have clear options to select when prompted
2. I want to be able to read the rules of the game
3. I want to personalise the game and enter my name
4. I want to be able to log-in if I return to the game
5. I want to receive a real time feedback throughout the game
6. I want to get a feedback after each answer
7. I want to be able to play multiple games when I'm logged in
8. I want to see my score

### Site Owner

9. I want users to have a positive experience whilst playing the game
10. I want users to easily navigate the game
11. I want user accounts to be saved to Google Spreadsheet
12. I want the user to get feedback in case of wrong input
13. I want data entry to be validated, to guide the user on how to correctly format the input

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flowchart

The following flowchart summarises the structure and logic of the application.

<details><summary>Flowchart</summary>
<img src="docs/flowchart_higher_lower.png">
</details>

## Technologies Used

### Languages

- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools

- [Lucid.net](https://lucid.app/) was used to draw program flowchart
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Cloud Platform](https://cloud.google.com/cloud-console/) was used to manage access and permissions to the Google Services such as Google auth, sheets etc.
- [Google Sheets](https://www.google.co.uk/sheets/about/) were used to store users details
- [Word Population API](https://rapidapi.com/aldair.sr99/api/world-population/) Used to get all countries populations
- [Heroku Platform](https://dashboard.heroku.com/) was used to deploy the project into live environment
- [PEP8](http://pep8online.com/) was used to check my code against Python conventions
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
VSCode was used to write the project code using Code Institute template

### Libraries

#### Python Libraries
- random - used to shuffle the country list
- time - used to displayed delayed messages in the terminal
- [unittest](https://docs.python.org/3/library/unittest.html) - used to carry out testing on single units in code_testing.py file

#### Third Party Libraries
- [requests](https://pypi.org/project/requests/) - Used to access the API data in a json format
- [colorama](https://pypi.org/project/colorama/) - I used this library to add color to the terminal and enhance user experience. I marked warning/error information with color red and user feedback with blue and green
- [pwinput](https://pypi.org/project/pwinput/) - Used to hide characters when the user enters the password
- [gspread](https://docs.gspread.org/en/latest/) - I used gspread to add and manipulate data in my Google spreadsheet and to interact with Google APIs
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - Module used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function. A creds.json file is created with all details the API needs to access the google account. In deployment to heroku this information is stored in the config var section.

[Back to Table Of Contents](#table-of-contents)

## Features

### Welcome message

- Provides user with a welcome message
- Gives user option to log-in or to create a new account
- User stories covered: 9
 
<details>
    <summary>Welcome Screenshot</summary>

![Welcome message](docs/features/welcome.png)
</details>

### Game Instructions
- Displays clear simple game instructions
- User stories covered: 2
  
<details>
    <summary>Game instructions Screenshot</summary>

![Game instructions](docs/features/game-rules.png)
</details>

### Log-in
- Asks users for their username
- Informs them if the username in not registered
- Asks users for their passcode
- Gives users alternative to start over and create a new account if can not remenber the passcode
- If correct, access their data from the Google Spreadsheet
- User stories covered: 3, 4

<details>
    <summary>Log-in Screenshot</summary>

![Log-in-1](docs/features/log-in-1.png)
![Log-in-2](docs/features/log-in-2.png)
![Log-in-3](docs/features/log-in-3.png)
</details>

<details>
    <summary>Alternative Log-in Screenshot</summary>

![Log-in wrong username](docs/features/alternative-log-in-1.png)
![Log-in wrong passcode](docs/features/alternative-log-in-2.png)
</details>

### Account creation
- Asks user for a new username and a passcode
- Validates user input values
- Informs user if the username is already taken
- User account will be saved to Google Spreadsheet after creation
- User stories covered: 3, 11, 13

<details>
    <summary>Account creation Screenshot</summary>

![Account creation](docs/features/new-account-1.png)
![Account creation](docs/features/new-account-2.png)
![Account creation](docs/features/new-account-3.png)
</details>

<details>
    <summary>Account creation Validation Screenshot</summary>

![Account creation Validation](docs/features/new-account-error-1.png)
![Account creation Validation](docs/features/new-account-error-2.png)
</details>

### Game
- Displays the question
- Player is asked to type yes or no
- Display warning message if user typed a wrong input
- Provide feedback on the user answer
- Show the populations of the countries from the question with the wrong answer
- Gives options to play again after finished game
- Display the score and feedback on the play performance
- User stories covered: 1, 5, 6, 7, 8, 10, 12

<details>
    <summary>Game Screenshot</summary>

![Game screen](docs/features/game-1.png)
![Game screen](docs/features/game-2.png)
![Game screen](docs/features/game-3.png)
</details>

<details>
    <summary>Wrong input in Game Screenshot</summary>

![Wrong input in Game screen](docs/features/game-error-1.png)
</details>

#### HeighScores
- Display the top five heighscores

<details>
    <summary>Height Scores Screenshot</summary>

![HeighScores](docs/features/heighscores.png)
</details>

### User Input Validation
- Displays an error message if user input is not in a form that was expected
- Asks for a new input and provides guidance to user on how to correctly format the input
- User stories covered: 
