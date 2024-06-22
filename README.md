# Hangman-Game

## Overview
This project implements the classic Hangman game in Python with a unique twist. Players try to guess a hidden word by suggesting letters within a certain number of guesses. Unlike the original game, there is no hangman figure. Instead, players start with 10 points, and each incorrect guess deducts one point. If the player reaches zero points, they lose. Correct guesses of letters that appear multiple times in the word will increase the player's point tally. Players can also choose to guess the whole word at once.

## Features
- Random word selection from a predefined list.
- Text-based user interface.
- Keeps track of guessed letters and remaining points.
- Displays the progress of the word being guessed.
- Allows players to guess the whole word.
- Simple and intuitive game flow.

## How to Play
1. The game randomly selects a word from a list.
2. The player guesses one letter at a time or chooses to guess the whole word.
3. Correct guesses reveal the letter's position(s) in the word and can increase the point tally.
4. Incorrect guesses deduct one point from the starting 10 points.
5. The game ends when the word is guessed correctly or the player runs out of points.

## Running the Game
- Open your terminal or command prompt.
- Navigate to the directory where the game files are located.
- Run the game by executing the hangman.py file

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or support, please open an issue on the GitHub repository or contact the project maintainer.
