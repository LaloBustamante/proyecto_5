import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# Crea un encabezado
st.header("Análisis de datos de vehículos")

# Variables para almacenar las selecciones del usuario
columna_histograma = st.selectbox("Selecciona una columna para el histograma:", car_data.columns, key='columna_histograma')
eje_x_dispersion = st.selectbox("Selecciona el eje X para el diagrama de dispersión:", car_data.columns, key='eje_x_dispersion')
eje_y_dispersion = st.selectbox("Selecciona el eje Y para el diagrama de dispersión:", car_data.columns, key='eje_y_dispersion')

# Función para generar el histograma
def generar_histograma():
    fig = px.histogram(car_data, x=st.session_state.columna_histograma)
    st.plotly_chart(fig)

# Función para generar el diagrama de dispersión
def generar_dispersion():
    if not pd.api.types.is_numeric_dtype(car_data[st.session_state.eje_x_dispersion]):
        st.error(f"La columna '{st.session_state.eje_x_dispersion}' no es numérica. Seleccione una columna numérica para el eje X.")
        return
    if not pd.api.types.is_numeric_dtype(car_data[st.session_state.eje_y_dispersion]):
        st.error(f"La columna '{st.session_state.eje_y_dispersion}' no es numérica. Seleccione una columna numérica para el eje Y.")
        return
    fig = px.scatter(car_data, x=st.session_state.eje_x_dispersion, y=st.session_state.eje_y_dispersion)
    st.plotly_chart(fig)

# Botón para generar el histograma
if st.button("Generar histograma"):
    generar_histograma()
# Casilla de verificación para el histograma
if st.checkbox("Construir histograma"):
    generar_histograma()

# Botón para generar el diagrama de dispersión
if st.button("Generar diagrama de dispersión"):
    generar_dispersion()
# Casilla de verificación para el histograma
if st.checkbox("Construir diagrama de dispersión"):
    generar_dispersion()

