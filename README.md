Prédiction du Défaut de Paiement des Clients
Ce projet permet de prédire une réponse d'acceptation ou de refus d'un client, en fonction de son score de défaut de paiement en utilisant un modèle de machine learning. 
L'application est déployée sur Azure et permet d'interagir avec une API pour obtenir des prédictions basées sur les données client.

Fonctionnalités
API de Prédiction : Une API REST qui permet de prédire si un client est accepté ou refusé pour un crédit, en retournant un score de probabilité de défaut de paiement.
Tests Unitaires : Des tests unitaires sont mis en place avec unittest pour garantir le bon fonctionnement des fonctionnalités.
Explication des Prédictions : Utilisation de bibliothèques comme SHAP pour fournir des explications des prédictions.

Structure du Projet
Voici un aperçu des fichiers et dossiers principaux :
app.py : Le fichier principal de l'application qui contient la logique de prédiction et l'API Flask.
logistic_model.pkl : Le modèle de régression logistique utilisé pour faire les prédictions.
subset_clients.csv : Un fichier de données clients utilisé pour tester les prédictions.
test_api.py : Contient les tests unitaires pour vérifier que l'API fonctionne correctement et que l'API retourne les résultats attendus.
utils_fonction_cout.py : Fichier utilitaire pour gérer les fonctions liées aux prédictions.
utils_threshold.py : Fichier utilitaire pour gérer les seuils de décision dans les prédictions.
.github/workflows : Dossier contenant les workflows GitHub Actions pour l'intégration continue (CI), incluant l'exécution des tests unitaires à chaque commit.

Déploiement sur Azure
Ce projet est déployé sur Azure via GitHub Actions, ce qui permet une intégration continue et un déploiement automatique à chaque commit. Vous pouvez accéder à l'API déployée à l'URL suivante :
https://webappscoringcredit-gcbhe8axc2exdfge.francecentral-01.azurewebsites.net
