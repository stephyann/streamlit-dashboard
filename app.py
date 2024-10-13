import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("Simple Dashboard with Streamlit")

# Description de l'application
st.write("""
Cette application génère un tableau de données aléatoires que vous pouvez filtrer en fonction d'une valeur.
""")

# Générer des données aléatoires
np.random.seed(42)
data = pd.DataFrame({
    'A': np.random.randint(1, 100, 100),
    'B': np.random.randn(100),
    'C': np.random.randint(10, 500, 100)
})

# Affichage des données dans Streamlit
st.write("Voici les données générées :")
st.dataframe(data)

# Slider pour filtrer les données
filter_value = st.slider("Filtrer les valeurs de la colonne A", 0, 100, 50)

# Filtrer les données
filtered_data = data[data['A'] > filter_value]
st.write(f"Les données où la colonne A est supérieure à {filter_value} :")
st.dataframe(filtered_data)

# Graphique simple
st.write("Histogramme des valeurs de la colonne B :")
st.bar_chart(filtered_data['B'])
