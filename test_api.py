# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:06:04 2024

Tests unitaires
"""

import unittest
import requests
import random
import pandas as pd

# URL de ton API
BASE_API_URL = "https://appcredit-h3emgjc7a5f9d5hp.northeurope-01.azurewebsites.net/predict"

# Charger les clients depuis le fichier subset_clients.csv avec id_client en tant qu'index
def get_random_client_id():
    df = pd.read_csv("subset_clients.csv")
    df.set_index('SK_ID_CURR', inplace=True)  # Lire le fichier CSV et utiliser la colonne id_client comme index
    return random.choice(df.index.tolist())  # Sélectionner un id_client aléatoire depuis l'index

class TestPredictAPI(unittest.TestCase):
    
    def test_predict_random_client(self):
        """Test de prédiction pour un client aléatoire du fichier"""
        id_client = get_random_client_id()  # Récupère un id_client aléatoire
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