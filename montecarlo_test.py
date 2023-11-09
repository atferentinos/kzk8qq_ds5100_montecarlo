import unittest
import pandas as pd
import numpy as np

from Demo.montecarlo import Die, Game, Analyzer

class TestDieMethods(unittest.TestCase):
    def test_init_die(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(test_faces)
        self.assertIsInstance(die.show_state(), pd.DataFrame)
        
    def test_change_weight(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(test_faces)
        die.change_weight(1, 2.5)
        self.assertEqual(die.show_state().loc[1, 'weights'], 2.5)
        
    def test_roll(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(test_faces)
        outcomes = die.roll(10)
        self.assertEqual(len(outcomes), 10)
        
    def test_show_state(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(test_faces)
        state = die.show_state()
        self.assertIsInstance(state, pd.DataFrame)

class TestGameMethods(unittest.TestCase):
    def test_init_game(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        self.assertIsInstance(game.dice_list, list)
        
    def test_play(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        game.play(5)
        self.assertIsNotNone(game.show_results())
        
    def test_show_results(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        game.play(5)
        results = game.show_results()
        self.assertIsInstance(results, pd.DataFrame)

class TestAnalyzerMethods(unittest.TestCase):
    def test_analyzer(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        game.play(5)
        analyzer = Analyzer(game)
        
    def test_combo_count(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        game.play(5)
        analyzer = Analyzer(game)
        combos = analyzer.combo_count()
        self.assertIsInstance(combos, pd.DataFrame)
        
    def test_face_counts_per_roll(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        game.play(5)
        analyzer = Analyzer(game)
        counts = analyzer.face_counts_per_roll()
        self.assertIsInstance(counts, pd.DataFrame)
        
    def test_permutation_count(self):
        test_faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(test_faces)
        die2 = Die(test_faces)
        game = Game([die1, die2])
        game.play(5)
        analyzer = Analyzer(game)
        perms = analyzer.permutation_count()
        self.assertIsInstance(perms, pd.DataFrame)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)