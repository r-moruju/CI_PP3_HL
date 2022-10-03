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

## User Stories

### Users

1. I want to have clear options to select when prompted
2. I want to be able to read the rules of the game
3. I want to personalise the game and enter my name
4. I want to be able to log-in if I return to the game
5. I want to receive a real time feedback throughout the game
6. I want to get a feedback when I win the game
7. I want to be able to play multiple games when I'm logged in
8. I want to see my score

### Site Owner

9. I want users to have a positive experience whilst playing the game
10. I want users to easily navigate the game
11. I want user accounts to be saved to Google Spreadsheet
12. I want the user to get feedback in case of wrong input
13. I want data entry to be validated, to guide the user on how to correctly format the input