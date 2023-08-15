# Tutorial Datasets con Hugging Face


En este tutorial vamos a crear nuestro propio conjunto de datos utilizando
la plataforma Hugging Face 🤗. Si siguen todas las instrucciones van a desbloquear la hábilidad de crear repositorios para sus conjuntos de datos y cargarlos con la librería [`datasets`](https://huggingface.co/docs/datasets/index) en python usando una simple
línea de código.

¿Qué es Hugging Face (aka HF)? Es una start-up de Inteligencia Artificial fundada el año 2016 que dispone de una plataforma (o hub) para compartir modelos de machine learning, datasets, y aplicaciones. Además, desarrolla y mantiene distintas herramientas de código abierto para interactuar con la plataforma, y facilitar el entrenamiento, _fine-tuning_ de modelos, y compartir prototipos a través de _end-points_ de inferencia o demos (e.g. Gradio o Streamlit). Originalmente conocida por la popular librería [`transformer`](https://huggingface.co/docs/transformers/index) para modelos de Procesamiento de Lenguaje Natural, o NLP por su sigla en inglés, la cual se ha expandido rápidamente para cubrir otros campos como Visión por Computadora, Audio, entre otros. Esta librería es popular entre investigadores y desarrolladores por ser una de las primeras
en abstraer y tomar ventaja (de manera seria) de los modelos pre-entrenados. Finalmente, tanto la librería como la plataforma se hicieron muy conocidas por el libro [_Natural Language Processing with Transformers. Building Language Applicationos with Hugging Face_](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/), donde uno de los co-autores es tambien uno de sus co-fundadores.


⚠️  Antes de comenzar el tutorial asegurate de  contar con una cuenta personal en [Hugging Face](https://huggingface.co/), puedes crearte una cuenta (sin costo) siguiendo las instrucciones desde el sitio web.

## Motivación

Comencemos con un conjunto de datos ya existente, veamos de qué se trata todo esto,  y luego exploremos cómo descargar y cargarlos en un Google Colab.

_Introducing (🥁)...the [`croupier-mtg-dataset`](https://huggingface.co/datasets/alkzar90/croupier-mtg-dataset) 🎆!_ Cada observación es una imagen de una mítica criatura del popular juego de cartas coleccionables [_Magic the Gathering_](https://es.wikipedia.org/wiki/Magic:_El_encuentro). Si no tienes idea de lo que estoy hablando, no importa, solo basta saber que es un juego de cartas tipo Pokémon, y que lucen de la siguiente forma:

<p align="center">
<img src="./assets/527518_elf.png" width="223" height="311" alt="Magic the Gathering card: Shessra, Death's Whisper">
</p>

Después de una arbitraria curatoría para seleccionar un grupo de cartas de criaturas y
procesar las imágenes de las cartas para solo capturar la región que contiene la ilustración, 
obtenemos el conjunto de imágenes que será nuestro dataset \o/. Otra información
que vamos a utilizar será el tipo de criatura, si observas con mayor atención
en la imagen de la carta anterior, _"Shessra, Death's Whisper"_, entre la ilustración
y el cuadro donde aparece la mayor proporción de texto, hay una línea de texto 
que dice _"Legendary Creature - Human Elf Warlock"_. Si las `X`'s de nuestro dataset son
imágenes, los `y`'s serán las etiquetas indicando si la criatura es un elfo, caballero,
trasgo, o zoombie 🧟‍♀️. Ahhhh! Todo esto va a terminar en un modelo 
que tomara imágenes y las clasificará en tipos de criatura?! Claro que no, el
objetivo es construir el dataset, pero el resto te debería resultar bastante
más sencillo!


<p align="center">
<img src="./assets/croupier-mtg-dataset.png" width="450" height="450" alt="A set of Magic the Gathering card ilustrations">
</p>

Sin entrar en mayores detalles, este grupo de imágenes (archivos `.png` o `.jpg`) se subió [a este repositorio de la plataforma Hugging Face](https://huggingface.co/datasets/alkzar90/croupier-mtg-dataset), que al dar _click_ llegaran a una página que tiene la siguiente estructura:


<p align="center">
<img src="./assets/croupier-repo-screenshot.png" width="760" height="525" alt="A screenshot that shows the croupier dataset in Hugging Face">
</p>

Personalmente me resulta fácil pensar la página que tenemos delante  como una especie
de repositorio de GitHub, pero enfocado en conjunto de datos. Algunas
observaciones sobre su contenido:

* (A): Se indica el nombre del repositorio para buscarlo dentor del hub de conjunts de datos en Hugging Face (si no es privado). Importante, esos cuadritos al lado del nombre, permiten copiar la ruta
del repositorio (i.e. `alkzar90/croupier-mtg-dataset`). El corazón son los _likes_ del repositorio, como a nadie le interesa mi repositorio, tiene 0 _likes_.
* (B): En esta línea podemos ver las opciones `Dataset card` (especie de README en GitHub), de hecho, un archivo README permite editar esta especie de página con text y otra meta data de nuestro dataset. Luego, esta la opción `Files`, acá es la estructura de carpetas donde estan nuestros archivos, si das _click_ podrás navegar por los archivos y datos que se encuentra en el repositori. `Community` por ahora piensenlo como una página para mantener comunicación, levantar _issues_, o solicitar aclaraciones sobre el conjunto de datos. `Settings` son las configuraciones de su repositorio, acá pueden desde fijar la opción de privacidad, hasta borrarlo.
* (C): Una de las cosas geniales de este repositorio es que cuenta con un visualizador
del conjunto de datos. Si se utiliza una forma estandar de organizar los datos, la página
automáticamente despliega una muestra del conjunto de datos. En el ejemplo, podemos ver un
par de observacones, puros elfos...
* (D): Información adicional, como el número de descargas del último mes, página web o repositorio si se indica, opciones para obtener el código y cargar el conjunto de datos en Python. 

De hecho, al darle _click_ al botón _Use in dataset library_, se despliega un recuadro con
el siguiente código:

```python
from datasets import load_dataset

dataset = load_dataset("alkzar90/croupier-mtg-dataset")
```

Si, _spoiler_, así se carga el maldito dataset.




## Crear un nuevo dataset


<p align="center">
<img src="./assets/hf-new-dataset.png" width="650" height="525" alt="A screenshot that shows the 'new dataset' option in a HF profle">
</p>
