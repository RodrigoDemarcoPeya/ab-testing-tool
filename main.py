import streamlit as st
from stats_engine import HypothesisTester
from explicaciones import obtener_explicacion
from biblioteca import teoria_estadistica  

st.set_page_config(page_title="A/B Testing Analyzer", layout="centered")

st.title("📊 Herramienta de A/B Testing")

tab_calculadora, tab_biblioteca = st.tabs(["🧮 Calculadora de A/B Test", "📚 Biblioteca Teórica"])

# ==========================================
# PESTAÑA 1: LA CALCULADORA 
# ==========================================
with tab_calculadora: 
    tester = HypothesisTester(alpha=0.05)
    # --- SELECTOR DE MODALIDAD ---
    modalidad = st.selectbox(
        "Selecciona la Modalidad de Análisis",
        ("Proporciones (Ej: Tasa de Conversión)", "Medias - T-Test (Ej: Ticket Promedio)", "Medias - Z-Test (Gigantes)")
    )

    # --- MÓDULO EDUCATIVO ---
    info = obtener_explicacion(modalidad)
    if info:
        with st.expander("🧠 Aprender más sobre esta prueba"):
            st.subheader(info["titulo"])
            st.write("**¿Cómo funciona?**")
            st.write(info["como_funciona"])
            st.write("**¿Cuándo usarla?**")
            st.write(info["cuando_usar"])

    st.divider()

    # --- INPUTS ---
    col1, col2 = st.columns(2)

    with col1:
        n_a = st.number_input("Tamaño de muestra (N) - Control", min_value=1, value=1000)
    with col2:
        n_b = st.number_input("Tamaño de muestra (N) - Variación", min_value=1, value=1000)

    if "Proporciones" in modalidad:
        with col1:
            val_a = st.number_input("Proporción A (Ej: 0.15)", min_value=0.0, max_value=1.0, value=0.10)
        with col2:
            val_b = st.number_input("Proporción B (Ej: 0.15)", min_value=0.0, max_value=1.0, value=0.12)
    else:
        with col1:
            val_a = st.number_input("Media A", value=100.0)
            std_a = st.number_input("Desviación Estándar A", min_value=0.1, value=15.0)
        with col2:
            val_b = st.number_input("Media B", value=105.0)
            std_b = st.number_input("Desviación Estándar B", min_value=0.1, value=15.0)

    # --- BOTÓN DE ANÁLISIS ---
    if st.button("Analizar Resultados 🚀", type="primary"):
        if "Proporciones" in modalidad:
            resultado = tester.z_test_proportions(val_a, val_b, n_a, n_b)
        elif "T-Test" in modalidad:
            resultado = tester.t_test_means(val_a, val_b, std_a, std_b, n_a, n_b)
        else:
            resultado = tester.z_test_means(val_a, val_b, std_a, std_b, n_a, n_b)

        st.subheader("Resultados")
        if resultado["is_significant"]:
            st.success(f"✅ **DIFERENCIA SIGNIFICATIVA** (p-value: {resultado['p_value']:.4f})")
        else:
            st.warning(f"❌ **NO SIGNIFICATIVO** (p-value: {resultado['p_value']:.4f})")
            
        st.write(f"**Estadístico:** {resultado['statistic']:.4f} | **Diferencia (B-A):** {resultado['diff']:.4f}")


# ==========================================
# PESTAÑA 2: LA BIBLIOTECA (Tu Google Doc)
# ==========================================
with tab_biblioteca:
    st.header("📚 Diccionario de Estadística y Experimentación")
    st.write("Consulta rápida de los conceptos más importantes para el análisis de A/B Testing.")
    
    # Recorremos el diccionario que creamos en biblioteca.py para armar la interfaz
    for categoria, conceptos in teoria_estadistica.items():
        with st.expander(f"📚 {categoria}", expanded=False):
            for concepto, definicion in conceptos.items():
                with st.expander(f"📌 {concepto}"):
                    st.markdown(definicion)
                    
        st.divider()