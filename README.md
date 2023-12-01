
# Alexandra Ferentinos MonteCarlo Simulation 

This project is for the DS5100 UVA graduate course final project and deliverables. This project is the culimation of DS5100 course work, emphasizing the following: Basic syntax, expressions, and statements in Python. Python Classes with initialization methods. Data manipulation with Numpy and Pands. Literate programming with docstrings and documentation. Unit testing with Unittest. Simple plotting with Pandas. Program modularization and packaging with setuptools. GitHub for managing and sharing code.  This project implements a simple Monte Carlo simulator using a set of three related classes -- a Die Class, a Game Class, and an Analyzer class. 


# Installation, once in file path 
pip install -e .
    
## Demo

```python
from Demo.montecarlo import Die, Game, Analyzer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test_faces = np.array([1, 2, 3, 4, 5, 6])
die1 = Die(test_faces)
die2 = Die(test_faces)
die2.change_weight(1,2)
print(die2.roll())
die2.roll()
game = Game([die1, die2])
game.play(5)
print(game.play_results())
analyzer = Analyzer(game)
amount_jackpots = analyzer.jackpot()
counts = analyzer.face_counts()
combos = analyzer.combo_faces()
perms = analyzer.distinct_permutations()
print(amount_jackpots)
print(counts)
print(combos)
print(perms)
```




## API Description

### Die Class

#### `__init__(self, N: np.ndarray) -> None`
- Initializes a Die with face data.

  ##### Parameters:
  - `N` (np.ndarray): Array of faces of the die.

  ##### Raised errors:
  - `TypeError`: Throws a TypeError if not a Numpy array.
  - `ValueError`: Tests to see if the values are distinct and raises ValueError if not.

#### `change_weight(self, N: int, new_weight: Union[int, float, str]) -> None`
- A method to change the weight of a single side.

  ##### Parameters:
  - `N` (int): Face value to be changed.
  - `new_weight` (Union[int, float, str]): The weight of the face value that was changed.

  ##### Raises:
  - `IndexError`: If the face value is not valid.
  - `TypeError`: If weight is not numeric (integer or float) or castable numeric.

#### `roll(self, rolls: int = 1) -> List[int]`
- A method to roll the die one or more times.

  ##### Parameters:
  - `rolls` (int): Number of times the die is to be rolled; defaults to 1.

  ##### Returns:
  - List[int]: A Python list of outcomes.

#### `current_state(self) -> pd.DataFrame`
- Dies current state.

  ##### Returns:
  - pd.DataFrame: A copy of the private die data frame.

### Game Class

#### `__init__(self, dies: List[Die]) -> None`
- Initializes a Game with face data. Takes a single parameter, a list of already instantiated similar dice.

  ##### Parameters:
  - `dies` (List[Die]): A list of already instantiated similar dice.

#### `play(self, rolls: int) -> None`
- Play method how many times dice should be rolled.

  ##### Parameters:
  - `rolls` (int): Integer parameter specifying how many times dice should be rolled.

#### `play_results(self, form: str = 'wide') -> pd.DataFrame`
- Results of the most recent play.

  ##### Parameters:
  - `form` (str): Parameter to return the data frame in narrow or wide form. Defaults to wide.

  ##### Returns:
  - pd.DataFrame: Results of the most recent play.

### Analyzer Class

#### `__init__(self, game: Game) -> None`
- Takes a game object as its input parameter. Throws a ValueError if the passed value is not a Game object.

  ##### Parameters:
  - `game` (Game): Game object as a parameter.

  ##### Raises:
  - `ValueError`: If the passed value is not a Game object.

#### `jackpot(self) -> int`
- A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.

  ##### Returns:
  - int: Number of times the game resulted in a jackpot.

#### `rolled_event(self) -> pd.DataFrame`
- Computes how many times a given face is rolled in each event.

  ##### Returns:
  - pd.DataFrame: Data frame of results.

#### `combo_faces(self) -> pd.DataFrame`
- Computes the distinct combinations of faces rolled, along with their counts.

  ##### Returns:
  - pd.DataFrame: Data frame of results.

#### `distinct_permutations(self) -> pd.DataFrame`
- Computes the distinct permutations of faces rolled, along with their counts.

  ##### Returns:
  - pd.DataFrame: Data frame of results.


## Running Tests, in correct file path 

To run tests, run the following command

```bash
  python montecarlo_test.py 2> montecarlo_results.txt
```

