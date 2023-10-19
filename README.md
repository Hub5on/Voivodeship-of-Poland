# Poland Voivodeships Game

This is a simple Python turtle graphics game that allows you to guess the names of Polish voivodeships on a map. The game reads voivodeship data from a CSV file and displays an image of the map for you to guess the names.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python packages if you haven't already:
``pip install pandas``
3. Place the `voivodeships.csv` and `map.gif` file in the same directory as the Python script.

## How to Play

1. Run the Python script `main.py`.
2. A window will open with the map of Polish voivodeships.
3. Try to guess the names of the voivodeships and type them into the prompt that appears.
4. If you guess a voivodeship correctly, it will be displayed on the map, and you'll be prompted to guess another.
5. The game continues until you've guessed all the voivodeships.

## Data Source

The voivodeship data is loaded from the `voivodeships.csv` file, which contains a list of Polish voivodeships along with their coordinates.

## Requirements

- Python 3
- pandas
- turtle
