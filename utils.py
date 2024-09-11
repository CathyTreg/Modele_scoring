# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:19:59 2024

@author: druar
"""

# utils.py
from sklearn.metrics import confusion_matrix

def cout_metier(y_true, y_pred):
    """Cette fonction calcule le coût métier à partir de la matrice de confusion : 10*FN + FP."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return 10 * fn + fp