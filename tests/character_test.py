import unittest

import character

class TestCharacter(unittest.TestCase):
    
    # init : tester que toutes les variables sont bien crees
    def test_initialization(self):
        c = character.Character({ "x": 13, "y": 4 }, 32, 12)

        self.assertEqual(c.position["x"], 13)
        self.assertEqual(c.position["y"], 4)
        self.assertEqual(c.health_points, 32)
        self.assertEqual(c.mana_points, 12)

    # move : tester les 4 directions de deplacement
    def test_move(self):
        c = character.Character({ "x": 13, "y": 4 }, 32, 12)

        c.move("up")
        self.assertEqual(c.position["x"], 13)
        self.assertEqual(c.position["y"], 5)

        c.move("left")
        self.assertEqual(c.position["x"], 12)
        self.assertEqual(c.position["y"], 5)

        c.move("down")
        self.assertEqual(c.position["x"], 12)
        self.assertEqual(c.position["y"], 4)

        c.move("right")
        self.assertEqual(c.position["x"], 13)
        self.assertEqual(c.position["y"], 4)

    # attack : tester que la vie du 2e personnage descend de la valeur des degats
    def test_attack(self):
        c1 = character.Character({ "x": 10, "y": 5 }, 20, 10)
        c2 = character.Character({ "x": 15, "y": 3 }, 10, 30)
        c1.attack(c2, 5)
        self.assertEqual(c2.health_points, 5)

    # use_spell : tester que les points de mana sont utilises
    def test_use_spell(self):
        c = character.Character({ "x": 13, "y": 4 }, 32, 12)
        c.use_spell("boule de feu", 5)
        self.assertEqual(c.mana_points, 7)