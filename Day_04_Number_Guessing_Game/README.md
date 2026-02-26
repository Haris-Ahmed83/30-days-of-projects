# Day 04 - Number Guessing Game

## Project Description

This is a simple command-line interface (CLI) number guessing game. The program selects a random number between 1 and 100, and the user has to guess it. The program provides hints (too high or too low) until the user guesses the correct number.

## Features

*   **Random Number Generation**: Generates a random number between 1 and 100.
*   **User Input**: Prompts the user to enter their guess.
*   **Hints**: Provides feedback if the guess is too high or too low.
*   **Attempt Counter**: Keeps track of the number of attempts.
*   **Error Handling**: Handles invalid input (non-numeric guesses).

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd "Day_04_Number_Guessing_Game"
    ```

2.  **Run the game**:

    ```bash
    python3 number_guessing_game.py
    ```

## Usage

Upon running the script, you will be prompted to guess a number. Enter your guess and press Enter. The game will provide hints until you guess the correct number.

### Example Workflow

```
Welcome to the Number Guessing Game!
I have selected a number between 1 and 100. Can you guess it?
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 30
Too low! Try again.
Enter your guess: 33
Congratulations! You guessed the number 33 in 5 attempts!
```
