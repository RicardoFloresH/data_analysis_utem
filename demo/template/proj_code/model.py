"""
    model.py: modulo donde se especifica el modelo
"""
from sklearn.linear_model import LogisticRegression

RND_STATE=42

modelo_clasificacion = LogisticRegression(random_state=RND_STATE)


