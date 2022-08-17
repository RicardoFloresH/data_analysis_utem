"""
    dataset.py: modulo para cargar y pre-procesar datos.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

DATA_SOURCE = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
COLUMN_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
TEST_SIZE=0.33
RND_STATE=42


def load_dataset(URL=DATA_SOURCE):
    """Descarga desde el repositorio UCI el dataset iris y retorna una tupla con los siguientes dataframes:
     X_train, X_test, y_train, y_test."""
    print("Datos cargados con éxito")
    df = pd.read_csv(URL, names=COLUMN_NAMES, header=None)
    X, y = df.iloc[:, 0:4], df.iloc[:, [4]]
    labels = {key: id for key, id in zip(y.species.unique(), [x for x in range(3)])}
    y = y.replace({"species": labels}).squeeze()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RND_STATE)
    return X_train, X_test, y_train, y_test, labels
