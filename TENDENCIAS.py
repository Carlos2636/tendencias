import pandas as pd
import streamlit as st

# === Cargar datos base ===
df = pd.read_excel("suma_por_carrera_2024.xlsx")

# === Título ===
st.title("Referencia Facultad - Ingresos 2024")

# === Selección de Carrera ===
carrera = st.selectbox("Selecciona una carrera:", df['Carrera'].unique())
resumen = df[df['Carrera'] == carrera].iloc[0]

# === Entradas del usuario ===
st.markdown("### Consulta del usuario")
consulta_total = st.number_input("Consulta Total Ingresos", min_value=0.0, value=0.0, step=1000.0)
consulta_12 = st.number_input("Consulta Ventas 12%", min_value=0.0, value=0.0, step=1000.0)
consulta_0 = st.number_input("Consulta Ventas 0%", min_value=0.0, value=0.0, step=1000.0)

# === Función de cálculo corregida: (consulta * 15%) / referencia_facultad ===
def calcular_porcentaje(consulta, referencia):
    if referencia == 0:
        return 0.0
    resultado = (consulta * 0.15) / referencia
    return min(resultado, 0.15)

# === Cálculo individual ===
resultado_total = calcular_porcentaje(consulta_total, resumen['2024_TOTAL']) * 100
resultado_12 = calcular_porcentaje(consulta_12, resumen['2024_VENTAS_12']) * 100
resultado_0 = calcular_porcentaje(consulta_0, resumen['2024_VENTAS_0']) * 100

# === Promedio final ===
promedio = (resultado_total + resultado_12 + resultado_0) / 3

# === Resultados ===
st.markdown("### Resultados")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Referencia Facultad")
    st.metric("Total Ingresos", f"${resumen['2024_TOTAL']:,.0f}")
    st.metric("Ventas 12%", f"${resumen['2024_VENTAS_12']:,.0f}")
    st.metric("Ventas 0%", f"${resumen['2024_VENTAS_0']:,.0f}")

with col2:
    st.markdown("#### Resultado (%)")
    st.metric("Total Ingresos", f"{resultado_total:.2f}%")
    st.metric("Ventas 12%", f"{resultado_12:.2f}%")
    st.metric("Ventas 0%", f"{resultado_0:.2f}%")

# === Resultado final ===
st.markdown("---")
st.markdown(f"### ✅ Resultado Final: **{promedio:.2f}%**")

