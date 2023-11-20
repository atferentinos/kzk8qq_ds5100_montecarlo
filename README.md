# kzk8qq_ds5100_montecarlo
DS5100 Final Project 
# Alexandra Ferentinos Monte Carlo Simulator

## Metadata
- **Author:** Alexandra Ferentinos
- **Project:** Monte Carlo Simulator, Fall 2023 DS5100

## Synopsis

```python
# Installation, once in file path 
!pip install -e .
# Defaulting to user installation because normal site-packages is not writeable
Obtaining file:///sfs/qumulo/qhome/kzk8qq/Documents/MSDS/DS5100/kzk8qq_ds5100_montecarlo
Requirement already satisfied: pandas in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from Demo==0.1) (1.1.3)
Requirement already satisfied: numpy in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from Demo==0.1) (1.19.2)
Requirement already satisfied: matplotlib in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from Demo==0.1) (3.3.2)
Requirement already satisfied: python-dateutil>=2.7.3 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from pandas->Demo==0.1) (2.8.1)
Requirement already satisfied: pytz>=2017.2 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from pandas->Demo==0.1) (2020.1)
Requirement already satisfied: kiwisolver>=1.0.1 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from matplotlib->Demo==0.1) (1.3.0)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from matplotlib->Demo==0.1) (2.4.7)
Requirement already satisfied: certifi>=2020.06.20 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from matplotlib->Demo==0.1) (2021.10.8)
Requirement already satisfied: pillow>=6.2.0 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from matplotlib->Demo==0.1) (8.0.1)
Requirement already satisfied: cycler>=0.10 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from matplotlib->Demo==0.1) (0.10.0)
Requirement already satisfied: six>=1.5 in /sfs/applications/202307/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages (from python-dateutil>=2.7.3->pandas->Demo==0.1) (1.15.0)
Installing collected packages: Demo
  Attempting uninstall: Demo
    Found existing installation: Demo 0.1
    Uninstalling Demo-0.1:
      Successfully uninstalled Demo-0.1
  Running setup.py develop for Demo
Successfully installed Demo

# Import
import numpy as np
import pandas as pd 
from Demo.montecarlo import Die, Game, Analyzer

# 1: Create Dice example
faces = np.array([1, 2, 3, 4, 5, 6])
my_die = Die(faces)

# weight change of face
my_die.change_weight(1, 0.5)

# Roll the die
outcomes = my_die.roll(10)

# Create game with multiple dice
dice_list = [Die(np.array([1, 2, 3, 4, 5, 6])) for _ in range(3)]
my_game = Game(dice_list)

# 2: Play a Game example 
my_game.play(11)

# 3: Analyze a Game example 
analyzer = Analyzer(my_game)
jackpot_count = analyzer.jackpot()
rolled_event_counts = analyzer.rolled_event()
combo_faces_counts = analyzer.combo_faces()
distinct_permutations_counts = analyzer.distinct_permutations()

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
