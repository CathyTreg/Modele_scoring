# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:38:17 2024

@author: druar
"""

# utils_threshold.py
from utils_fonction_cout import cout_metier
import numpy as np

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