# -*- coding: utf-8 -*-
"""
APP Flask
"""
# Imports
import numpy as np
from sklearn.metrics import confusion_matrix, make_scorer
import joblib
from flask import Flask, request, jsonify

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

# Charger le modèle
model = joblib.load('modele_logRegression.pkl')

# Récupérer le meilleur modèle et la partie classification
best_model = model.best_estimator_
logistic_model = best_model.named_steps['classification']


# Initialiser l'application Flask
app = Flask(__name__)

# Définir un endpoint pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données envoyées dans la requête POST
    data = request.get_json(force=True)
    
    # Extraire les caractéristiques et les convertir en tableau NumPy
    features = np.array(data).reshape(1, -1)
    
    # Faire une prédiction
    prediction = logistic_model.predict(features)
    
    # Vérifier le résultat de la prédiction et retourner le message approprié
    result = "crédit accepté" if int(prediction[0]) == 0 else "crédit refusé"
    
    # Retourner le résultat sous forme de JSON
    return jsonify({'prediction': result})

# Définir un endpoint de test pour s'assurer que l'API fonctionne
@app.route('/', methods=['GET'])
def home():
    return "API de prédiction de régression logistique est opérationnelle!"

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)