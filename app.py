import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Proyecto ETL - Notas Estudiantes", layout="wide")

# Título y encabezado
st.title("Explorador de Datos de Ingeniería")
st.write("Bienvenido al dashboard de análisis de hardware y software.")

# Barra lateral para parámetros
with st.sidebar:
    st.header("Configuración")
    nombre_estudiante = st.text_input("Nombre del Estudiante")
    archivo = st.file_uploader("Sube tu archivo Parquet o CSV", type=['parquet', 'csv'])

# Lógica principal
if archivo is not None:
    if archivo.name.endswith('.parquet'):
        df = pd.read_parquet(archivo)
    else:
        df = pd.read_csv(archivo)

    st.success(f"Archivo cargado con éxito por {nombre_estudiante}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Filas", len(df))
    col2.metric("Columnas", len(df.columns))
    col3.metric("Memoria (KB)", df.memory_usage().sum() // 1024)

    st.subheader("Vista Previa de los Datos")
    st.dataframe(df.head(10))

    st.subheader("Gráfico Interactivo")
    columnas = df.select_dtypes(include=[np.number]).columns.tolist()
    if columnas:
        eje_x = st.selectbox("Selecciona el eje X", columnas)
        st.line_chart(df[eje_x])
else:
    st.info("Esperando que se cargue un archivo de datos...")