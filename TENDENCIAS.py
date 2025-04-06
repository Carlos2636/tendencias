import pandas as pd
import streamlit as st

# === Estilo general ===
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #000000;
        }
        .main {
            background-color: #ffffff;
        }
        h1, h3, h4 {
            color: #660000;
        }
        .stMetric {
            background-color: #f5f5f5;
            border-radius: 10px;
            padding: 10px;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# === Cargar datos base ===
df = pd.read_excel("suma_por_carrera_2024.xlsx")

# === Título ===
st.markdown("""
    <div style='background-color: #660000; padding: 10px 20px; border-radius: 8px;'>
        <h1 style='color: white;'>Mercado</h1>
    </div>
""", unsafe_allow_html=True)

# === Selección de Carrera ===
st.markdown("<h4 style='margin-top: 30px;'>Selecciona una carrera:</h4>", unsafe_allow_html=True)
carrera = st.selectbox("", df['Carrera'].unique())
resumen = df[df['Carrera'] == carrera].iloc[0]

# === Entradas del usuario ===
st.markdown("<h4 style='margin-top: 30px;'>Consulta del usuario</h4>", unsafe_allow_html=True)
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
st.markdown("<h4 style='margin-top: 30px;'>Resultados</h4>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h5 style='color: #660000;'>Referencia Facultad</h5>", unsafe_allow_html=True)
    st.metric("Total Ingresos", f"${resumen['2024_TOTAL']:,.0f}")
    st.metric("Ventas 12%", f"${resumen['2024_VENTAS_12']:,.0f}")
    st.metric("Ventas 0%", f"${resumen['2024_VENTAS_0']:,.0f}")

with col2:
    st.markdown("<h5 style='color: #660000;'>Resultado (%)</h5>", unsafe_allow_html=True)
    st.metric("Total Ingresos", f"{resultado_total:.2f}%")
    st.metric("Ventas 12%", f"{resultado_12:.2f}%")
    st.metric("Ventas 0%", f"{resultado_0:.2f}%")

# === Resultado final ===
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='background-color: #660000; padding: 10px 20px; border-radius: 8px;'>
        <h2 style='color: white;'>✅ Resultado Final: {promedio:.2f}%</h2>
    </div>
""", unsafe_allow_html=True)

