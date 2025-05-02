This project implements Conway's Game of Life - a simple zero-player game.

The Game of Life follows simple rules where the state of each cell evolves with every generation based on the states of its neighbors. The rules are:
1. A live cell dies from underpopulation if it has less than two live neighbours
2. A live cell dies from overpopulation if it has more than three live neighbours
3. A dead cell becomes alive when surrounded by exactly three live neighbours
4. A live cell survives if it has two or three live neighbours

This version allows user to:
- pause game - press the **Space** bar (**Game starts paused**)
- randomize the board - press the **R** key
- clear the board (kill all cells) - press the **Z** key (only when paused)
- Toggle state of individual cells - **left click** (only when paused)

After downloading this repository, you can run the game locally. Make sure you have Python 3.9 or newer installed.
To install required dependencies run following command (use virtual environment if possible):

    pip install -r requirements.txt

If you're using [uv](https://github.com/astral-sh/uv) for package management you can simply run the project with: 

    uv run main.py
