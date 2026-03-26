import streamlit as st
from stats_engine import HypothesisTester
from biblioteca import teoria_estadistica  

# Configuración de página
st.set_page_config(page_title="A/B Testing Analyzer", layout="wide", page_icon="📊")

# Estilos personalizados para mejorar la visualización
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Herramienta de A/B Testing")
st.caption("Una plataforma educativa y profesional para el análisis de experimentos.")

tab_calculadora, tab_biblioteca = st.tabs(["🧮 Calculadora de A/B Test", "📚 Biblioteca Teórica"])

# ==========================================
# PESTAÑA 1: LA CALCULADORA 
# ==========================================
with tab_calculadora: 
    # --- CONFIGURACIÓN GLOBAL ---
    with st.sidebar:
        st.header("⚙️ Configuración")
        alpha = st.slider("Nivel de Significancia (α)", min_value=0.01, max_value=0.20, value=0.05, step=0.01)
        st.info(f"El test rechazará la hipótesis nula si el p-value es menor a {alpha}")
        
    tester = HypothesisTester(alpha=alpha)
    
    # --- SELECTOR DE MODALIDAD ---
    modalidad = st.selectbox(
        "Selecciona la Modalidad de Análisis",
        (
            "Proporciones (Ej: Tasa de Conversión)", 
            "Medias - T-Test (Welch - Recomendado)", 
            "Medias - Z-Test (Muestras Gigantes)"
        )
    )

    # --- MÓDULO EDUCATIVO ---
    mapa_biblioteca = {
        "Proporciones": "Proporciones",
        "T-Test": "Medias (T - Test)",
        "Z-Test": "Z Test"
    }
    
    info_key = next((v for k, v in mapa_biblioteca.items() if k in modalidad), None)
    if info_key:
        with st.expander("🧠 ¿Cuándo usar esta prueba?"):
            st.markdown(teoria_estadistica["5. Modalidades de análisis"][info_key])

    st.divider()

    # --- INPUTS ---
    col_input_a, col_input_b = st.columns(2)

    with col_input_a:
        st.subheader("Grupo A (Control)")
        n_a = st.number_input("Tamaño de muestra (N) - A", min_value=1, value=1000, key="na")
    with col_input_b:
        st.subheader("Grupo B (Variación)")
        n_b = st.number_input("Tamaño de muestra (N) - B", min_value=1, value=1000, key="nb")

    if "Proporciones" in modalidad:
        with col_input_a:
            val_a = st.number_input("Tasa de Conversión A (0.0 - 1.0)", min_value=0.0, max_value=1.0, value=0.10, format="%.4f")
        with col_input_b:
            val_b = st.number_input("Tasa de Conversión B (0.0 - 1.0)", min_value=0.0, max_value=1.0, value=0.12, format="%.4f")
    else:
        with col_input_a:
            val_a = st.number_input("Media A", value=100.0)
            std_a = st.number_input("Desviación Estándar A", min_value=0.001, value=15.0)
        with col_input_b:
            val_b = st.number_input("Media B", value=105.0)
            std_b = st.number_input("Desviación Estándar B", min_value=0.001, value=15.0)

    # --- BOTÓN DE ANÁLISIS ---
    if st.button("Analizar Resultados 🚀", type="primary", use_container_width=True):
        try:
            if "Proporciones" in modalidad:
                resultado = tester.z_test_proportions(val_a, val_b, n_a, n_b)
            elif "T-Test" in modalidad:
                resultado = tester.t_test_means(val_a, val_b, std_a, std_b, n_a, n_b)
            else:
                resultado = tester.z_test_means(val_a, val_b, std_a, std_b, n_a, n_b)

            # --- VISUALIZACIÓN DE RESULTADOS ---
            st.divider()
            st.subheader(f"Resultados: {resultado['test_name']}")
            
            # Métricas principales
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Diferencia (B-A)", f"{resultado['diff']:.4f}")
            with m2:
                st.metric("P-Value", f"{resultado['p_value']:.4f}")
            with m3:
                st.metric("Estadístico", f"{resultado['statistic']:.2f}")

            if resultado["is_significant"]:
                st.success(f"✅ **DIFERENCIA SIGNIFICATIVA**: Hay suficiente evidencia estadística para rechazar la hipótesis nula con un α de {alpha}.")
            else:
                st.warning(f"❌ **NO SIGNIFICATIVO**: La diferencia observada probablemente se deba al azar. No se puede rechazar la hipótesis nula.")
                
        except ValueError as e:
            st.error(f"⚠️ Error en los datos: {e}")
        except Exception as e:
            st.error(f"🚨 Error inesperado: {e}")


# ==========================================
# PESTAÑA 2: LA BIBLIOTECA 
# ==========================================
with tab_biblioteca:
    st.header("📚 Diccionario de Estadística y Experimentación")
    st.write("Consulta rápida de los conceptos más importantes para el análisis de A/B Testing.")
    
    # Grid de categorías
    for categoria, conceptos in teoria_estadistica.items():
        with st.expander(f"📁 {categoria}", expanded=False):
            for concepto, definicion in conceptos.items():
                st.markdown(f"#### 📌 {concepto}")
                st.markdown(definicion)
                st.markdown("---")