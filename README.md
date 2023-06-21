# Lab - Class 06

## Project: ten-thousand

Author: Sarah Glass, Logan Reese, and Slava Makeev for Python 401

## Overview

Create a command line version of the dice game Ten Thousand.

Today is all about tackling the highest risk and/or highest priority features - scoring and dice rolling.

- Define a GameLogic class in ten_thousand/game_logic.py file.

- Handle calculating score for dice roll

- Add calculate_score static method to GameLogic class.

- The input to calculate_score is a tuple of integers that represent a dice roll.

- The output from calculate_score is an integer representing the roll’s score according to rules of game.


**Handle rolling dice**

- Add roll_dice static method to GameLogic class.

- The input to roll_dice is an integer between 1 and 6.

- The output of roll_dice is a tuple with random values between 1 and 6.

- The length of tuple must match the argument given to roll_dice method.

- Using the parameters above, use ChatGPT to generate code blocks.

- You must document every single line of code with a detailed description of what the code is doing.

## Links and Resources

- Lots of TA and peer help.
- Referenced class demo
- Chat GPT - prompts and output are documented in the "chatgpt.md" file

## Setup

No .env requirements; gitignore invludes venv.

## How to initialize/run your application

- python3 game_logic.py
- python3 test_ten_thousand.py

## How to use your library

No external libraries were brought in.

## Tests

All acceptance testing run through test_series.py file and pytest following TDD.
