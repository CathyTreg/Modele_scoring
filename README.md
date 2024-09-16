# Prédiction du Défaut de Paiement des Clients

Ce projet permet de prédire une réponse d'acceptation ou de refus d'un crédit pour un client, en fonction de sa probabilité de défaut de paiement en utilisant un modèle de machine learning. 
L'application est déployée sur **Azure** et permet d'interagir avec une API pour obtenir des prédictions basées sur les données client.

## 🛠️ Fonctionnalités

- **API de prédiction** : Une API REST qui permet de prédire si un client est accepté ou refusé pour un crédit, en retournant un score de probabilité de défaut de paiement.
- **Tests unitaires** : Des tests unitaires sont mis en place avec unittest pour garantir le bon fonctionnement des fonctionnalités.
- **Explication des prédictions** : Utilisation de bibliothèques comme **SHAP** pour fournir des explications des prédictions.

## 📁 Structure du projet

Voici les fichiers et répertoires les plus importants du projet :

- **`app.py`** : Le fichier principal de l'application qui contient la logique de prédiction et l'API Flask.
- **`logistic_model.pkl`** : Modèle de régression logistique utilisé pour les prédictions.
- **`subset_clients.csv`** : Ensemble de données clients utilisé pour les tests.
- **`test_api.py`** : Fichier contenant les tests unitaires pour l'API.
- **`utils_fonction_cout.py`** : Fichier utilitaire pour gérer les fonctions liées aux prédictions.
- **`utils_threshold.py`** : Fichier utilitaire pour gérer les seuils de décision dans les prédictions.
- **`.github/workflows/`** : Dossier contenant les workflows GitHub Actions pour l'intégration continue (CI), incluant l'exécution des tests unitaires à chaque commit.

## 🌐 Déploiement sur Azure

Le projet est déployé automatiquement sur **Azure** à l'aide de **GitHub Actions**. Cela permet une intégration continue (CI) et un déploiement rapide à chaque commit.

- Vous pouvez accéder à l'API déployée à l'URL suivante : https://webappscoringcredit-gcbhe8axc2exdfge.francecentral-01.azurewebsites.net
- Pour faire une prédiction pour un client, modifiez l'id_client à la fin de l'URL : https://webappscoringcredit-gcbhe8axc2exdfge.francecentral-01.azurewebsites.net/predict?client_id=398791

## 📈 Modèle de Machine Learning

Le modèle utilisé pour les prédictions est une régression logistique entraînée sur un jeu de données de clients. Les prédictions sont expliquées grâce à la librairie SHAP qui permet d'interpréter les résultats pour chaque client.

## 📝 Auteur
Ce projet a été développé par CathyTreg. Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter.
