import unittest
from unittest import result

from . import message 

class TestMessage(unittest.TestCase):
    
       def test_bonjour_mon_nom(self):
              result= "Bonjour, sondes"
              result = message.bonjour("sondes")
              self.assertEqual(result, "bonjour,sondes")
    
       def test_bonjour_mon_nom(self):
              result = message.bonjour("sondes")
              self.assertEqual(result, "Bonjour, sondes")  # Corrige moi mon code

    
       def test_compter(self):
              result = message.compter_mots 
              result = message.compter_mots("bonjour et bien venu")
              self.assertEqual(result, 4)
       
       #tester le cas ou le mdp est correct
       #si on lui donne "passeword" "st que on recupere
       #bien "autorisé"" 
     
       def test_mot_de_passe_correct(self):
              # Test avec un mot de passe correct
              resultat = message.verifier_mdp("password")
              self.assertEqual(resultat,"autorisé")

       def test_mot_de_passe_incorrect(self):
              # Test avec un mot de passe incorrect
              resultat = message.verifier_mdp("azerty")
              self.assertEqual(resultat,"interdit")
     
