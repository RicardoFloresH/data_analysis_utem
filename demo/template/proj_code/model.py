"""
    model.py: modulo donde se especifica el modelo
"""
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

RND_STATE=42


def reg_logistica(X, y):
    """Documentación de este modelo: """
    clf = LogisticRegression(random_state=RND_STATE)
    return clf.fit(X, y)


def gaussian_naive_bayes(X, y):
    """Documentación de este modelo: https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB
    .html """
    clf = GaussianNB()
    return clf.fit(X, y)

