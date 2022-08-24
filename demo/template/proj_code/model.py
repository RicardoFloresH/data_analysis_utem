"""
    model.py: modulo donde se especifica el modelo
"""
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

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


def reg_lineal(X, y):
    """Documentación de este modelo: """
    reg = LinearRegression()
    return reg.fit(X, y)

def reg_KNN(X, y, num_vecinos=5):
    """Documentación de este modelo: """
    reg = KNeighborsRegressor(n_neighbors=num_vecinos)
    return reg.fit(X, y)


