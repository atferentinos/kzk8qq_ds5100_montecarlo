import numpy as np
import pandas as pd

class Die:
    def __init__(self, N, W=None, is_coin=False):
        """
        A class representing a die.

        Args:
        - N (np.array): NumPy array of faces of the die.
        - W (np.array, optional): NumPy array of weights for each face.
        - is_coin (bool, optional): Boolean indicating if the die is a coin.
        
        Raises:
        - TypeError: If N is not a NumPy array.
        - ValueError: If N values are not unique.
        """
        if not isinstance(N, np.ndarray):
            raise TypeError("N must be a NumPy array.")

        if len(N) != len(np.unique(N)):
            raise ValueError("N values must be unique.")

        if W is None:
            W = np.ones(len(N))
        else:
            if len(W) != len(N):
                raise ValueError("Weights must have the same length as faces.")
            if any(weight < 0 for weight in W):
                raise ValueError("Weights must be non-negative.")

        self._data = pd.DataFrame({'weights': W}, index=N)
        self.is_coin = is_coin

    def change_weight(self, face, new_weight):
        """
        Changes the weight of a single side.

        Args:
        - face: Face value to be changed.
        - new_weight: The weight of the face value that was changed.

        Raises:
        - IndexError: If the face value is not valid.
        - TypeError: If the weight is not a non-negative number.
        """
        if face not in self._data.index:
            raise IndexError("Face value not valid.")

        if not (isinstance(new_weight, (int, float)) and new_weight >= 0):
            raise TypeError("Weight value is not a non-negative number.")

        self._data.loc[face, 'weights'] = new_weight

    def roll(self, times=1):
        """
        Simulates rolling the die one or more times.

        Args:
        - times: How many times the die should be rolled (default is 1).

        Returns:
        - A list of outcomes.
        """
        if self.is_coin:
            if len(self._data) != 2:
                raise ValueError("A coin must have exactly 2 faces.")
        return np.random.choice(
            self._data.index,
            size=times,
            p=self._data['weights'] / np.sum(self._data['weights'])
        ).tolist()

    def show_state(self):
        """
        Shows the current state of the die.

        Returns:
        - A copy of the private die data frame.
        """
        return self._data.copy()

class Game:
    def __init__(self, dice_list):
        """
        A class representing a game of rolling one or more dice.

        Args:
        - dice_list (list): List of already instantiated similar dice.

        Raises:
        - ValueError: If the list does not contain Die objects or if the dice do not have the same faces.
        """
        if not all(isinstance(die, Die) for die in dice_list):
            raise ValueError("The list must contain Die objects.")

        face_lengths = [len(die._data) for die in dice_list]
        if not all(length == face_lengths[0] for length in face_lengths):
            raise ValueError("All dice must have the same number of faces.")

        self.dice_list = dice_list
        self._data = None

    def play(self, times):
        """
        Simulates playing the game by rolling the dice a specified number of times.

        Args:
        - times (int): Number of times the dice should be rolled.

        Returns:
        - None
        """
        results = {}
        for idx, die in enumerate(self.dice_list):
            results[f'die_{idx}'] = die.roll(times)
        self._data = pd.DataFrame(results)

    def show_results(self, form='wide'):
        """
        Shows the results of the most recent play.

        Args:
        - form (str): Parameter to return the data frame in narrow or wide form (defaults to wide form).

        Returns:
        - A copy of the private play data frame in the specified form.

        Raises:
        - ValueError: If the user passes an invalid option for narrow or wide.
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
            raise ValueError("Invalid option passed, choose 'wide' or 'narrow'.")   

class Analyzer:
    def __init__(self, game):
        """
        A class representing an Analyzer object that analyzes the results of a single game.

        Args:
        - game (Game): The input game object.

        Raises:
        - ValueError: If the passed value is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Passed value is not a Game Object!!")
        self.game = game

    def jackpot(self):
        """
        Computes the number of jackpots in the game.

        Returns:
        - An integer for the number of jackpots.
        """
        data = self.game.show_results()
        jackpots = (data == data.iloc[:, 0]).all(axis=1).sum()
        return jackpots

    def face_counts_per_roll(self):
        """
        Computes the number of times a given face is rolled in each event.

        Returns:
        - A data frame of results in wide format.
        """
        data = self.game.show_results()
        counts = data.apply(pd.Series.value_counts)
        return counts

    def combo_count(self):
        """
        Computes the distinct combinations of faces rolled, along with their counts.

        Returns:
        - A data frame of results with distinct combinations and associated counts.
        """
        data = self.game.show_results()
        combos = data.apply(lambda row: tuple(row), axis=1).value_counts()
        return pd.DataFrame(combos, columns=['counts'])

    def permutation_count(self):
        """
        Computes the distinct permutations of faces rolled, along with their counts.

        Returns:
        - A data frame of results with distinct permutations and associated counts.
        """
        data = self.game.show_results()
        perms = data.apply(lambda row: ''.join(map(str, row)), axis=1).value_counts()
        return pd.DataFrame(perms, columns=['counts'])


