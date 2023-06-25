# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8 --force

# Primera Carga a Github
# git init
# git add .
# git remote add origin https://github.com/nicoig/pygwalker.git
# git push -u origin master

# Actualizar Repo de Github
# git add .
# git commit -m "Se actualizan las variables de entorno"
# git push origin master

# Para eliminar un repo cargado
# git remote remove origin

# En Render
# agregar en variables de entorno
# PYTHON_VERSION = 3.9.12

import pandas as pd
import pygwalker as pyg
import streamlit as st
import csv

# Configuración de la página para usar el diseño amplio
st.set_page_config(layout="wide")

# Título de la página
st.title("Análisis de Datos con PyGWalker.")

# Inicialización del DataFrame
df = None

# Elección del archivo a través de la barra lateral
with st.sidebar:
    uploaded_file = st.file_uploader("Elige un archivo CSV o Excel", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.type == "text/csv":
            preview = uploaded_file.read(1024).decode()  # Lee los primeros 1024 bytes del archivo
            dialect = csv.Sniffer().sniff(preview)
            uploaded_file.seek(0)  # Regresa al inicio del archivo después de la previsualización
            df = pd.read_csv(uploaded_file, encoding='utf-8', delimiter=dialect.delimiter)
        else:
            st.error("El tipo de archivo no es compatible. Por favor, carga un archivo CSV o Excel.")

# Visualización con PyGWalker
if df is not None:
    pyg.walk(df, env='Streamlit', dark = "dark")


