"""
    dataset.py: modulo para cargar y pre-procesar datos.
    Devolver solo X e Y y mover el train_test_split...
"""

import pandas as pd

DATA_SOURCE = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
LOCAL_PATH = "./data/iris.data"
COLUMN_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]


def load_iris_web(URL=DATA_SOURCE):
    """Descarga desde el repositorio UCI el dataset iris y retorna un diccionario con el 'dataset', una tupla que
    contiene X (input) e y (output), además de las 'etiquetas'."""
    print("Datos cargados con éxito")
    df = pd.read_csv(URL, names=COLUMN_NAMES, header=None)
    X, y = df.iloc[:, 0:4], df.iloc[:, [4]]
    labels = {key: id for key, id in zip(y.species.unique(), [x for x in range(3)])}
    y = y.replace({"species": labels}).squeeze()
    return {"dataset": (X, y),
            "labels": labels}


def load_iris_local(PATH=LOCAL_PATH):
    """Cargar el dataset desde una ruta en disco local. Específicamente un archivo guardado en la carpeta ./data"""
    print("Datos cargados con éxito")
    return pd.read_csv(PATH, names=COLUMN_NAMES, header=None)

