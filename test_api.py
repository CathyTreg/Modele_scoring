# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:06:04 2024

Tests unitaires
"""

import unittest
import requests
import pandas as pd

# URL de ton API
BASE_API_URL = "https://appcredit-h3emgjc7a5f9d5hp.northeurope-01.azurewebsites.net/predict"

class TestPredictAPI(unittest.TestCase):
    
    def test_predict_random_client(self):
        """Test de prédiction pour un client du fichier"""
        id_client = 208550
        url = f"{BASE_API_URL}?client_id={id_client}"  # Construire l'URL avec le paramètre client_id
        
        # Envoyer une requête GET à l'API
        response = requests.get(url)

        # Vérifie que la requête a réussi
        self.assertEqual(response.status_code, 200)
        
        # Vérifie que la réponse est au format JSON et contient une clé appropriée
        response_data = response.json()
        self.assertTrue(any(key.startswith('prediction pour le client') for key in response_data.keys()))
        
        # Vérifie que la prédiction est soit "crédit accepté", soit "crédit refusé"
        prediction = next(iter(response_data.values()))  # Obtenir la première valeur de la réponse
        self.assertIn(prediction, ["credit accepte", "credit refuse"])

if __name__ == '__main__':
    unittest.main()