# Clasificador multiclase  , Keras  , TensorFlow

Este repositorio se enfoca en crear una pequeña App interactiva para podel clasificar el tipo de vidrio en base a la sus componentes , para tal fin usa un red neuronal profunda la cual ya ha sido entrenada con el conjunto de datos contenido en glass.csv , quedándonos con el mejor modelo ofrecido en dicho entrenamiento.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://glass-x0klpcvg3ij.streamlit.app/)

## Requisitos
A continuación se presentan las librerías necesarias para ejecutar este proyecto. Asegúrate de tenerlas instaladas en tu entorno.
```bash
streamlit==1.24.1
pandas==1.5.3
numpy==1.22.4
scikit-learn==1.2.2
lxml==4.9.2
tensorflow==2.12.0
keras== 2.12.0
```
## Estructura del Reposito
```bash
.
├── glass.csv               # conjunto de datos de entrenamiento
├── glass.py                # algoritmo de predicción
├── modelo_glass.py         # despliega el algoritmo de entrenamiento
├── mejor_modelo.h5         # Archivo con los mejores pesos de entrenamiento
├── norm_glass.pkl          # Archivo con las medidas de estandarización usadas
├── glass.py                # algoritmo de predicción
├── requirements.txt        # Lista de librerías requeridas
└── README.md               # Documentación del proyecto
```
## Uso
Selecciona loa valores de los componentes desde el panel lateral , la clasificación se realiza de forma automática .

## Créditos
Este proyecto utiliza las librerías de Python, incluyendo Streamlit, Pandas, NumPy, Matplotlib, Seaborn y Scikit-learn. Agradecimientos a la comunidad de desarrolladores de estas librerías.

