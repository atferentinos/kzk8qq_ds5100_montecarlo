
# Alexandra Ferentinos MonteCarlo Simulation 

This project is for the DS5100 UVA graduate course final project and deliverables. This project implements a simple Monte Carlo simulator using a set of three related classes -- a Die Class, a Game Class, and an Analyzer class. 


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

   ## API Description/Synopsis

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


## Running Tests

To run tests, run the following command

```bash
  python montecarlo_test.py 2> montecarlo_results.txt
```