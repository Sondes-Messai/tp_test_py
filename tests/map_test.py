import unittest

import character
import map

class TestMap(unittest.TestCase):
    
    # init : tester que toutes les variables sont bien crees
    def test_initialization(self):
        m = map.Map()
        self.assertEqual(len(m.characters), 0)

    # place : tester que la carte contient le personnage placce
    def test_place(self):
        m = map.Map()
        c = character.Character({ "x": 13, "y": 4 }, 32, 12)

        m.place(c)
        
        self.assertIn(c, m.characters)
    
    # are_same_place : tester que deux personnages sur la carte ayant
    # les memes coordonnees sont au meme endroit
    def test_are_same_place(self):
        m = map.Map()
        c1 = character.Character({ "x": 10, "y": 5 }, 20, 10)
        c2 = character.Character({ "x": 10, "y": 5 }, 10, 30)

        m.place(c1)
        m.place(c2)
        self.assertTrue(m.are_same_place(c1, c2))
    
    # are_same_place : tester que deux personnages sur la carte n'ayant
    # pas les memes coordonnees ne sont pas au meme endroit
    def test_are_not_same_place(self):
        m = map.Map()
        c1 = character.Character({ "x": 10, "y": 5 }, 20, 10)
        c2 = character.Character({ "x": 15, "y": 3 }, 15, 15)

        m.place(c1)
        m.place(c2)
        self.assertFalse(m.are_same_place(c1, c2))

    # are_same_place : tester que deux personnages, dont un pas sur
    # la carte, ne sont pas au meme endroit
    def test_are_same_place_but_not_on_map(self):
        m = map.Map()
        c1 = character.Character({ "x": 10, "y": 5 }, 20, 10)
        c2 = character.Character({ "x": 10, "y": 5 }, 10, 30)

        m.place(c1)
        self.assertFalse(m.are_same_place(c1, c2))
 
    # clear : tester que la carte est vide
    def test_clear(self):
        m = map.Map()
        c = character.Character({ "x": 13, "y": 4 }, 32, 12)

        m.place(c)
        m.clear()
        
        self.assertEqual(len(m.characters), 0)
        self.assertNotIn(c, m.characters)