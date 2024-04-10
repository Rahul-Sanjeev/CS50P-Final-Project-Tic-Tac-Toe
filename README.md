# Tic-Tac-Toe

#### Video Demo: https://youtu.be/IePdm4kLrVA?si=_E5dcKXA0jkep6Hl

## Description:

Welcome to the Tic-Tac-Toe project! This Python-based command-line game allows players to enjoy the classic Tic-Tac-Toe experience on their terminal. The game is designed to be intuitive, easy to play, and enjoyable for all ages.

## Project Structure:

### project.py:
This file contains the main logic for the Tic-Tac-Toe game. Here's a breakdown of the key functions:
- `main()`: The main function orchestrates the flow of the game, initializing the board, prompting players for their moves, and determining the winner or a draw.
- `display_board(board)`: This function displays the current state of the board to the console.
- `playerX_turn(board)`: Handles the turn for Player X, allowing them to input their move and updating the board accordingly.
- `playerO_turn(board)`: Handles the turn for Player O, similar to `playerX_turn()`.
- `is_valid(pos, board)`: Checks if a position chosen by a player is valid on the current board.
- `game_won(board)`: Determines if the game has been won by any player.
- `is_draw(board)`: Checks if the game has ended in a draw.

### test_project.py:
This file contains unit tests to validate the functionality of the functions in `project.py`. The tests cover various scenarios to ensure that the game logic behaves as expected.

## Design Choices:

### Simplicity and Readability:
The project emphasizes simplicity and readability of code to ensure that it's easy to understand and maintain. By using clear variable names and straightforward logic, the game becomes accessible to developers of all skill levels.

### Modularization:
The game logic is divided into separate functions, each responsible for a specific aspect of the game. This modular approach enhances code organization and facilitates testing and debugging.

### Input Validation:
The `is_valid()` function ensures that player inputs are valid positions on the board, preventing erroneous moves and enhancing the overall user experience.

### Test-Driven Development (TDD):
The inclusion of unit tests in `test_project.py` follows the Test-Driven Development approach. By writing tests before implementing functionality, we ensure that each feature behaves as expected and can be easily verified.

## Future Improvements:

### AI Opponent:
Implementing an AI opponent would enhance the game, allowing players to enjoy single-player mode against a computer-controlled opponent.

### Customization Options:
Adding support for customizing player names and board sizes would provide users with more flexibility and personalization options.

### Enhanced User Interface:
Improving the user interface with graphical elements or a graphical interface would make the game more visually appealing and engaging.

## Conclusion:

Tic-Tac-Toe is a timeless classic that continues to entertain people of all ages. With its simple yet elegant design, this Python implementation of the game brings the joy of Tic-Tac-Toe to the command line. Whether you're playing against a friend or challenging yourself in single-player mode, this project promises hours of fun and excitement.
