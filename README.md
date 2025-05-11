# Number Guessing Game

A simple command-line number guessing game implemented in Python where users attempt to guess a randomly generated number between 1 and 100.

## Description

This project is an interactive number guessing game where the computer randomly selects a number between 1 and 100, and the player tries to guess it. After each guess, the game provides feedback on whether the guess was too high or too low, helping the player narrow down the correct answer.

## Features

- Random number generation between 1 and 100
- Input validation for non-numeric entries
- Range validation (1-100)
- Feedback on each guess (too high/too low)
- Option to quit the game at any time

## Requirements

- Python 3.x
- NumPy 2.2.3
- Pandas 2.2.3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
   cd number-guessing-game
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
number-guessing-game/
├── main.py              # Main game logic
├── utils/
│   └── validation.py    # Input validation functions
├── requirements.txt     # Package dependencies
├── LICENSE              # MIT License
└── README.md            # This file
```

## Usage

Run the script using Python:

```bash
python main.py
```

How to play:
1. The program will generate a random number between 1 and 100
2. Enter your guess when prompted
3. Receive feedback on whether your guess is too high, too low, or correct
4. Continue guessing until you find the correct number
5. Enter 'q' at any time to quit the game

## Code Overview

The game uses:
- `random.randint()` for generating random numbers
- Custom validation function to check input validity
- NumPy and Pandas libraries (included but not fully utilized in the current version)
- Modular code structure with separate validation module

## Future Improvements

- Add difficulty levels (different ranges)
- Implement a scoring system based on number of attempts
- Track and display game statistics using Pandas
- Add a graphical user interface
- Add a maximum number of attempts
- Implement more advanced numerical analysis using NumPy and Pandas

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Yousef Rahimi - [yousefrahimi101@gmail.com](mailto:yousefrahimi101@gmail.com)

## Acknowledgments

- Inspired by classic number guessing games
- Built with Python's random module and custom validation