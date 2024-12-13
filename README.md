# Créer une API de scoring crédit et réaliser un DashBoard interactif

Projet Dashboard au lien : https://github.com/CathyTreg/Dashboard_credit

Contexte : L’entreprise « Prêt à dépenser » souhaite déployer un outil de scoring crédit pour calculer la probabilité qu’un client rembourse son crédit, en s’appuyant sur un modèle prédictif et un suivi en temps réel.

Objectif : Mettre en place un modèle de prédiction des risques de faillite client, intégrer ce modèle via une API pour une utilisation dans un système de scoring en production, et déployer un dashboard interactif pour l’analyse des clients.

Tâches :
-	Développement du modèle de scoring :
    - créer un modèle de régression logistique pour prédire la probabilité de défaut de paiement des clients ;
    - Implémenter un suivi de la performance du modèle via la surveillance du Data Drift avec Evidently et l'utilisation de SHAP pour expliciter les décisions du modèle.
-	Mise en production avec une API :
    - développer une API REST avec Flask permettant de recevoir des données et renvoyer des prédictions de scoring ;
    - déployer l'API en continu avec GitHub Actions via Azure WebApp pour garantir la mise à jour automatique du modèle en production ;
    -	créer des tests unitaires avec Unittest pour assurer la qualité et la stabilité du code via une exécution automatisée lors du déploiement.
-	Développement d’un Dashboard Interactif :
    - concevoir un dashboard interactif avec Streamlit permettant aux chargés d’études de visualiser la probabilité de solvabilité d’un client et d’interpréter les résultats du scoring en temps réel ;
    - mettre en place une interface utilisateur facilitant la compréhension des décisions du modèle grâce à des visualisations et des explications détaillées des prédictions.

Résultats : 
-	Évaluation en temps réel de la solvabilité des clients, fournissant des informations précises et expliquées à un chargé d’études, ce qui améliore la prise de décision dans l'octroi de crédits.
-	Grâce à l'intégration d'une approche MLOps, le modèle est facilement évolutif et peut être régulièrement mis à jour pour s'adapter aux nouvelles tendances et comportements clients.

Environnement de travail :
-	Outils de Développement : Jupyter Notebook, Python (via Anaconda), GitHub Actions
-	Outils de Machine Learning : Scikit-learn, MLFlow UI, Evidently (Data Drift), SHAP, Smote
-	Outils de déploiement et visualisation : Flask pour l'API, Azure WebApp, Streamlit pour le dashboard interactif, Unittest pour les tests automatisés.


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
