import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

# Crea un encabezado
st.header("Análisis de datos de vehiculos")

def generar_histograma():
  # Obtiene la columna que se quiere analizar a partir del input del usuario
  columna = st.selectbox("Selecciona una columna:", car_data.columns)

  # Crea el histograma con Plotly Express
  fig = px.histogram(car_data, x=columna)

  # Muestra el histograma
  st.plotly_chart(fig)

# Crea un botón y asóciale la función generar_histograma
boton_histograma = st.button("Generar histograma")

# Si se hace clic en el botón, ejecuta la función
if boton_histograma:
  generar_histograma()


def generar_dispersion():
    """
    Función para generar y mostrar el diagrama de dispersión.
    """

    # Obtiene las columnas seleccionadas para los ejes X e Y
    eje_x = st.selectbox("Selecciona el eje X:", car_data.columns)
    eje_y = st.selectbox("Selecciona el eje Y:", car_data.columns)

    # Verifica que las columnas existan y sean numéricas
    if not pd.api.types.is_numeric_dtype(car_data[eje_x]):
        st.error(f"La columna '{eje_x}' no es numérica. Seleccione una columna numérica para el eje X.")
        return

    if not pd.api.types.is_numeric_dtype(car_data[eje_y]):
        st.error(f"La columna '{eje_y}' no es numérica. Seleccione una columna numérica para el eje Y.")
        return

    # Crea el diagrama de dispersión con Plotly Express
    fig = px.scatter(car_data, x=eje_x, y=eje_y)

    # Muestra el diagrama de dispersión
    st.plotly_chart(fig)

    # Actualiza la vista para reflejar los cambios
    st.write("Diagrama actualizado")

# Crea un botón y asóciale la función generar_dispersion
boton_dispersion = st.button("Generar diagrama de dispersión")

# Si se hace clic en el botón, ejecuta la función
if boton_dispersion:
    generar_dispersion()


# Crea una casilla de verificación para el histograma
build_histogram = st.checkbox("Construir histograma")

if build_histogram:
  # Obtiene la columna que se quiere analizar a partir del input del usuario
  columna = st.selectbox("Selecciona una columna:", car_data.columns)

  # Crea el histograma con Plotly Express
  fig = px.histogram(car_data, x=columna)

  # Muestra el histograma
  st.plotly_chart(fig)