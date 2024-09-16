# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:06:04 2024

Tests unitaires
"""

import unittest
import requests

# URL de ton API
BASE_API_URL = "https://webappscoringcredit-gcbhe8axc2exdfge.francecentral-01.azurewebsites.net/predict"

class TestPredictAPI(unittest.TestCase):
    
    def test_predict_random_client(self):
        """Test de prédiction pour un client du fichier"""
        id_client = 144092
        url = f"{BASE_API_URL}?client_id={id_client}"  # Construire l'URL avec le paramètre client_id
        
        # Envoyer une requête GET à l'API
        response = requests.get(url)

        # Vérifie que la requête a réussi
        self.assertEqual(response.status_code, 200)
        
        # Vérifie que la réponse est au format JSON et contient les clés appropriées
        response_data = response.json()
        self.assertIn('probabilite_defaut (seuil=0.5)', response_data)
        self.assertIn('prediction', response_data)
        
        # Vérifie que la prédiction est soit "crédit accepté", soit "crédit refusé"
        prediction = response_data['prediction']
        self.assertIn(prediction, ["credit accepte", "credit refuse"])
        
        # Vérifie que 'probabilite_defaut (seuil=0.5)' est une liste de nombres
        self.assertIsInstance(response_data['probabilite_defaut (seuil=0.5)'], list)
        self.assertTrue(all(isinstance(x, float) for x in response_data['probabilite_defaut (seuil=0.5)']))

if __name__ == '__main__':
    unittest.main()