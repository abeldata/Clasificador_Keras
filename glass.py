import pandas as pd
import numpy as np
import streamlit as st
import pickle

from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model


# Cargar el MinMaxScaler desde el archivo pickle
with open('norm_glass.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Cargar el modelo entrenado
model = load_model('mejor_modelo.h5')



st.sidebar.markdown("""
                    ### Selecciona los valores
                    """)
 
def input_valores () :
    v_1 = st.sidebar.slider('idx_refraccion', 1.51115, 1.53393, 1.52101, step=0.00001, format='%.5f')
    v_2 = st.sidebar.slider('sodio', 10.73000, 17.38000, 13.64)
    v_3 = st.sidebar.slider('magnesio', 0.00000, 4.49000, 4.49)
    v_4 = st.sidebar.slider('aluminio', 0.34000, 3.50000, 1.10)
    v_5 = st.sidebar.slider('silicio', 69.81000, 75.41000,  71.78)
    v_6 = st.sidebar.slider('potasio', 0.00000, 6.21000, 0.06)
    v_7 = st.sidebar.slider('calcio', 5.43000, 16.19000, 8.75)
    v_8 = st.sidebar.slider('bario', 0.00000, 3.15000, 0.0)
    v_9 = st.sidebar.slider('hierro', 0.00000, 0.51000, 0.0)
    data = {'idx_refraccion' : v_1,
            'sodio' : v_2,
            'magnesio' : v_3,
            'aluminio' : v_4,
            'silicio' : v_5,
            'potasio' : v_6,
            'calcio' : v_7,
            'bario' : v_8,
            'hierro' : v_9,
            }
    features = pd.DataFrame(data, index=[0])
    return features 
df = input_valores()

# Main Panel

st.title("Clasificador de cristal")
st.markdown("""
       ## Clasificador multiclase ejecutado con Keras Tensor Flow
          Valores seleccionados
         """)





st.write(df)

# Escalar los datos
datos_escalados = scaler.transform(df)

# Diccionario tipos
nombres_tipos = {
    0 : 'vidrio flotado para ventanas de edificios',
    1 : 'vidrio no flotado para ventanas de edificios',
    2 : 'vidrio flotado para ventanas de vehículos',
    3 : 'contenedores',
    4 : 'vajillas',
    5 : 'faros de vehículos'
}

# Hacer predicción
prediccion = model.predict(datos_escalados)

st.header('Predicción del modelo')
clases_visualizacion = np.argmax(prediccion, axis=1) + 1
prediccion_mas1 = np.column_stack((clases_visualizacion, prediccion))
st.write(prediccion_mas1)


# Obtener las clases y probabilidades de la predicción
clase = int(np.argmax(prediccion, axis=1))
probabilidad = np.max(prediccion, axis=1)

# Crear un DataFrame con las clases y probabilidades
clases_map = nombres_tipos.get(clase)
prediccion_dataframe = pd.DataFrame({'Clase': clases_map, 'Porcentaje': probabilidad})


st.markdown("""
            #### Clase más probable
            """)
# Mostrar el DataFrame con las clases y probabilidades
st.write(prediccion_dataframe)