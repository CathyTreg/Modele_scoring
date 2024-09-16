# -*- coding: utf-8 -*-
"""
APP Flask
"""
# Imports
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, make_scorer
import joblib
from flask import Flask, jsonify, request
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from utils_fonction_cout import cout_metier
from utils_threshold import find_best_threshold

# Importer les données clients à prédire 
data_client = pd.read_csv('subset_clients.csv')
# mettre la colonne id client en index
data_client.set_index('SK_ID_CURR', inplace=True)
# Sauvegarder les noms des colonnes avant transformation
column_names = data_client.columns

# Transformer les données - centrer et réduire
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_client)

# Transformer les données - Imputer les valeurs manquantes avec la stratégie 'median'
imputer = SimpleImputer(strategy='median')
X_scaled_imputed = imputer.fit_transform(X_scaled)

# Transformer X_scaled_imputed en DataFrame et récupérer les colonnes d'origine
X_scaled_imputed_df = pd.DataFrame(X_scaled_imputed, index=data_client.index, columns=column_names)

# Charger le modèle 
logistic_model = joblib.load('logistic_model.pkl')

# Initialiser l'application Flask
app = Flask(__name__)

# Définir un endpoint pour la prédiction
@app.route('/predict', methods=['GET'])
def predict():
    # Récupérer le client_id depuis les paramètres de la requête
    client_id = request.args.get('client_id', type=int)
    
    if client_id is None:
        return jsonify({"error": "client_id manquant ou invalide"}), 400
    
    # Récupérer les données du client
    client = X_scaled_imputed_df.loc[client_id]
    
    # Extraire les caractéristiques et les convertir en tableau NumPy
    features = np.array(client).reshape(1, -1)
    
    # Faire une prédiction
    prediction = logistic_model.predict(features)
    
    # Vérifier le résultat de la prédiction et retourner le message approprié
    result = "credit accepte" if int(prediction[0]) == 0 else "credit refuse"
    
    # Retourner le résultat sous forme de JSON
    return jsonify({f'prediction pour le client {client_id}': result})

# Définir un endpoint de test pour s'assurer que l'API fonctionne
@app.route('/', methods=['GET'])
def home():
    return "API de prédiction de régression logistique est opérationnelle!"

# Lancer l'application Flask
if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)