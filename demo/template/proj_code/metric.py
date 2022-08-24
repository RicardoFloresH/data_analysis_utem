"""
    metric.py: Implementar las funciones de métrica y evaluación
"""
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.metrics import mean_squared_error, mean_absolute_error


def metrica_accuracy(y_verdad, y_preds):
    """Métrica de clasificación Accuracy"""
    return accuracy_score(y_verdad, y_preds)


def metrica_f1score(y_verdad, y_preds, avg='micro'):
    """Métrica de clasificación F1-score"""
    return f1_score(y_verdad, y_preds, average=avg)


def matriz_confusion(y_verdad, y_preds):
    """Obtener matriz de confusion"""
    return confusion_matrix(y_verdad, y_preds)


def metrica_mse(y_verdad, y_preds):
    """Métrica de regresión error cuadrático medio"""
    return mean_squared_error(y_verdad, y_preds)

def metrica_mae(y_verdad, y_preds):
    """Métrica de regresión error media absoluta"""
    return mean_absolute_error(y_verdad, y_preds)

