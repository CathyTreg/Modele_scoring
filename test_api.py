# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:06:04 2024

Tests unitaires
"""

import unittest
import requests
import pandas as pd

def cout_metier(y_true, y_pred):
    """Cette fonction calcule le coût métier à partir de la matrice de confusion : 10*FN + FP."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return 10 * fn + fp

cout_metier_scorer = make_scorer(cout_metier, greater_is_better=False)

def find_best_threshold(estimator, X, y):
    """Cette fonction trouve le seuil optimal en testant une gamme de seuils et en choisissant celui avec le score métier le plus bas."""
    thresholds = np.linspace(0, 1, 101)
    best_threshold, best_score = 0, float('inf')
    for threshold in thresholds:
        y_pred = (estimator.predict_proba(X)[:, 1] >= threshold).astype(int)
        score = cout_metier(y, y_pred)
        if score < best_score:
            best_threshold, best_score = threshold, score
    return best_threshold, best_score

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