import pandas as pd
import streamlit as st
 
# Cargar los resultados generados previamente

df = pd.read_excel("./suma_por_carrera_2024.xlsx")
 
# Título
st.title("Referencia Facultad - Ingresos 2024")
 
# Selector de carrera
carrera = st.selectbox("Selecciona una carrera:", df['Carrera'].unique())
 
# Filtrar los datos
resumen = df[df['Carrera'] == carrera].iloc[0]
 
# Mostrar los resultados en formato visual
st.markdown("### Resultados")
st.markdown(f"**Total Ingresos:** ${resumen['2024_TOTAL']:,.0f}")
st.markdown(f"**Ventas 12%:** ${resumen['2024_VENTAS_12']:,.0f}")
st.markdown(f"**Ventas 0%:** ${resumen['2024_VENTAS_0']:,.0f}")