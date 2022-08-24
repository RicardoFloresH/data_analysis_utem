"""
    dataset.py: modulo para cargar y pre-procesar datos.
    Devolver solo X e Y y mover el train_test_split...
"""

import pandas as pd

DATA_SOURCE = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
REGRESION_DATA_SOURCE = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

LOCAL_PATH = "./data/iris.data"
COLUMN_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
REGRESION_COLUMN_NAMES = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year",
                          "origin", "car_name"]


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


def load_auto_mpg_web(URL=REGRESION_DATA_SOURCE):
    """Descarga desde el repositorio UCI el dataset auto-mpg y retorna un diccionario con el 'dataset', una tupla que
    contiene X (input) e y (output)."""
    print("Datos cargados con éxito")
    df = pd.read_fwf(URL, names=REGRESION_COLUMN_NAMES, header=None)
    # X contiene todas las columnas excepto la primera (que es y) y la última que es el nombre del modelo del auto
    # y contiene la primera columna que es mpg
    X, y = df.iloc[:, 1:-1], df.iloc[:, [0]]
    # La columna horsepower se lee como string porque tiene algunas valores NA, dejar solo las observaciones que
    # tengan valores en todas las caracteristicas
    X["horsepower"] = pd.to_numeric(X["horsepower"], errors='coerce')
    non_missing_values = X["horsepower"].isna()
    # Ahora negamos el vector booleanos que nos indica los indices de observaciones NA para obtener los indices
    # de observaciones que la variables horsepower tiene valores
    X = X[~non_missing_values]
    y = y[~non_missing_values]
    return {"dataset": (X, y)}
