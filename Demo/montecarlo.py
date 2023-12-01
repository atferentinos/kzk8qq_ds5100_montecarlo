import numpy as np
import pandas as pd

    # test function, needs to throw type error if not a NumPy Array

class Die:

    """
    A class, changing faces and weights.

    Attributes:
    - faces(N) (np.array): Array of faces of the die.
    - _data (pd.DataFrame): Private data frame that stores the die weights.
    """
    def __init__(self, N):
        """
        Initializes a Die with face data.

        Args:
        - faces(N) (np.array): Array of faces of the die..

        Raised errors:
        - TypeError: Throws a TypeError if not a Numpy array.
        - ValueError: Test to see if the values are distinct and raise ValueError if not.
        """
        if not isinstance(N, np.ndarray):
            raise TypeError("Not a Numpy Array!!")

        if len(N) != len(np.unique(N)):
            raise ValueError("Faces values must be unique!!")

        self._data = pd.DataFrame({'weights': [1.0]*len(N)}, index=N)
        
    def change_weight(self, N, new_weight):
        """
        A method to change the weight of a single side.

        Args:
        - face(N): face value to be changed.
        - new_weight: the weight of face value that was changed.

        Raises:
        - IndexError: If the face value is not valid.
        - TypeError: If weight is not numeric (interger or float) or castable numeric.
        """
        if N not in self._data.index:
            raise IndexError("Face value not valid!!")

        if not (isinstance(new_weight, (int, float)) or str(new_weight).isnumeric()):
            raise TypeError("Weight value is not numeric!!")

        self._data.loc[N, 'weights'] = new_weight
        
    def roll(self, rolls=1):
        """
        method to roll the die one or more times.

        Args:
        - how many times the die is to be rolled; defaults to  1

        Returns:
        - Returns a Python list of outcomes.
        """
        ##not to internally store results
        return np.random.choice(self._data.index, size=rolls, p=self._data['weights']/np.sum(self._data['weights'])).tolist()
    
    def current_state(self):
        """
        Dies current state

        Returns:
        - Returns a copy of the private die data frame.
        """
        return self._data.copy()      
        
#Game Class
class Game:
    """
    A game consists of rolling of one or more similar dice (Die objects) one or more times

    Attributes:
    - list of already instantiated similar dice.
    """
    ##Takes a single parameter, a list of already instantiated similar dice
    def __init__(self, dies):
        """
        Initializes a Die with face data. Takes a single parameter, a list of already instantiated similar dice

        Args:
        - takes a single parameter, a list of already instantiated similar dice.
        """
        self.dies = dies
        self._data = None
        
##play method how many times dice should be rolled 
    def play(self, rolls):
        """
       play method how many times dice should be rolled

        Args:
        - interger parameter how many times dice should be rolled. 
        """
        results = {}
        for idx, die in enumerate(self.dies):
            results[f'die_{idx}'] = die.roll(rolls)
        self._data = pd.DataFrame(results)
        
##results of most recent play
    def play_results(self, form='wide'):
        """
        results of most recent play

        Args:
        - Takes a parameter to return the data frame in narrow or wide form which defaults to wide form.

        Raises:
        - ValueError:if the user passes an invalid option for narrow or wide.
        """
        if form == 'wide':
            if self._data is None:
                return pd.DataFrame()
            return self._data.copy()
        elif form == 'narrow':
            if self._data is None:
                return pd.DataFrame()
            else:
                return self._data.melt(ignore_index=False, var_name='die_number', value_name='outcomes')
        else:
            raise ValueError("Invalid option passed, choose 'wide' or 'narrow'!!")

##Analyzer class, Throw a ValueError if the passed value is not a Game object
class Analyzer:
    """
    An Analyzer object takes the results of a single game and computes various descriptive statistical properties about it.

    Attributes:
    - game object as parameter
    
    Raises:
    ValueError:  if the passed value is not a Game object
    """
    def __init__(self, game):
        """
        Takes a game object as its input parameter. Throw a ValueError if the passed value is not a Game object.

        Attributes:
        - game object as parameter
    
        Raises:
        ValueError:  if the passed value is not a Game object
        """
        if not isinstance(game, Game):
            raise ValueError("Passed value is not a Game Object!!")
        self.game = game
        
    ##jackpot method
    def jackpot(self):
        """
        A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.

        Args:
        - Computes how many times the game resulted in a jackpot.

        Returns:
        -Returns an integer for the number of jackpots.
        """
        return self.game.play_results().eq(self.game.play_results().iloc[:, 0], axis=0).all(1).sum()
    
    ##facecounts method
    def rolled_event(self):
        """
        Computes how many times a given face is rolled in each event.

        Functions
        The data frame has an index of the roll number, face values as columns, and count values in the cells (i.e. it is in wide format)

        Returns:
        -Returns a data frame of results.
        """
        data = self.game.play_results()
        counts = data.apply(pd.Series.value_counts)
        #may need to fix for Nan
        return counts

    ##A combo count method
    def combo_faces(self):
        """
        Computes the distinct combinations of faces rolled, along with their counts.

        Combinations are order-independent and may contain repetitions.

        Returns:
        -Returns a data frame of results.
        """
        data = self.game.play_results()
        combos = data.apply(lambda row: tuple(row), axis=1).value_counts()
        return pd.DataFrame(combos, columns=['counts'])
    
    ##An permutation count method
    def distinct_permutations(self):
        """
        Computes the distinct permutations of faces rolled, along with their counts.

        The data frame should have a MultiIndex of distinct permutations and a column for the associated counts

        Returns:
        -Returns a data frame of results.
        """
        data = self.game.play_results()
        perms = data.apply(lambda row: ''.join(map(str, row)), axis=1).value_counts()
        return pd.DataFrame(perms, columns=['counts'])

