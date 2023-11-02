# Clasificador multiclase  , Keras  , TensorFlow

Este repositorio se enfoca en crear una pequeña App interactiva para podel clasificar el tipo de vidrio en base a la sus componentes , para tal fin usa un red neuronal profunda la cual ya ha sido entrenada con glass.csv quedandonos con el mejor modelo ofrecido en dicho entrenamiento.

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
## Estructura del Repositorio UD3.ipynb
```bash
.
├──
├── glass.py                   # algoritmo de predicción
├── modelo_glass.py            # despliega el algoritmo de entrenamiento
├── mejor_modelo.h5            # Archivo con los mejores pesos de entrenamiento
├── norm_glass.pkl             # Archivo con las medidas de estandarización usadas
├── glass.py                   # algoritmo de predicción
├── requirements.txt           # Lista de librerías requeridas
└── README.md                  # Documentación del proyecto
```
