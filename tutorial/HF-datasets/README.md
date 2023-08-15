# Tutorial Datasets con Hugging Face


En este tutorial vamos a crear nuestro propio conjunto de datos utilizando
la plataforma Hugging Face 🤗. Si siguen todas las instrucciones van a desbloquear la hábilidad de crear repositorios para sus conjuntos de datos y cargarlos con la librería `datasets` en python usando una simple
línea de código.

¿Qué es Hugging Face (aka HF)? Es una start-up de Inteligencia Artificial fundada el año 2016 que dispone de una plataforma (o hub) para compartir modelos de machine learning, datasets, y aplicaciones. Además, desarrolla y mantiene distintas herramientas de código abierto para interactuar con la plataforma, y facilitar el entrenamiento, _fine-tuning_ de modelos, y compartir prototipos a través de _end-points_ de inferencia o demos (e.g. Gradio o Streamlit). Originalmente conocida por la popular librería [`transformer`](https://huggingface.co/docs/transformers/index) para modelos de Procesamiento de Lenguaje Natural, o NLP por su sigla en inglés, la cual se ha expandido rápidamente para cubrir otros campos como Visión por Computadora, Audio, entre otros. Esta librería es popular entre investigadores y desarrolladores por ser una de las primeras
en abstraer y tomar ventaja (de manera seria) de los modelos pre-entrenados. Finalmente, tanto la librería como la plataforma se hicieron muy conocidas por el libro [_Natural Language Processing with Transformers. Building Language Applicationos with Hugging Face_](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/), donde uno de los co-autores es tambien uno de sus co-fundadores.


⚠️  Antes de comenzar el tutorial asegurate de  contar con una cuenta personal en [Hugging Face](https://huggingface.co/), puedes crearte una siguiendo las instrucciones en su sitio web.

## Motivación

Comencemos con un conjunto de datos ya existente y exploremos primero cómo descargar y cargarlos en un Google Colab.

_Introducing (🥁)...the [`croupier-mtg-dataset`](https://huggingface.co/datasets/alkzar90/croupier-mtg-dataset) 🎆!_ Cada observación es una imagen de una mítica criatura del popular juego de cartas coleccionables [_Magic the Gathering_](https://es.wikipedia.org/wiki/Magic:_El_encuentro). Si no tienes idea de lo que estoy hablando, no importa, solo basta saber que es un juego de cartas tipo Pokemon, y que lucen de la siguiente forma:

<p align="center">
<img src="./assets/527518_elf.png" width="223" height="311" alt="Magic the Gathering card: Shessra, Death's Whisper">
</p>

Después de una arbitraria curatoría para seleccionar un grupo de cartas de criaturas y
procesar las imagenes de las cartas para solo capturar la región que contiene la ilustración, 
obtenemos el conjunto de imágenes que será nuestro dataset \o/

<p align="center">
<img src="./assets/croupier-mtg-dataset.png" alt="A set of Magic the Gathering card ilustrations">
</p>

Sin entrar en mayor detalles, este grupo de imagenes (archivos `.png` o `.jpg`) se subieron [a este repositorio de la plataforma Hugging Face](https://huggingface.co/datasets/alkzar90/croupier-mtg-dataset), que se ve de la siguiente forma:


<p align="center">
<img src="./assets/croupier-repo-screenshot.png" alt="A screenshot that shows the croupier dataset in Hugging Face">
</p>


## Crear un nuevo dataset


<p align="center">
<img src="./assets/hf-new-dataset.png" alt="A screenshot that shows the 'new dataset' option in a HF profle">
</p>
