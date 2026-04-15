import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, t
from stats_engine import HypothesisTester
from biblioteca import teoria_estadistica  

# Configuración de página
st.set_page_config(page_title="A/B Testing Analyzer", layout="wide", page_icon="📊")

# Estilos personalizados
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

def plot_test_results(resultado, alpha):
    """Genera un gráfico de la distribución con la región de rechazo y el estadístico."""
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Determinar qué distribución usar
    if "T-Test" in resultado['test_name']:
        dist_name = "T-Student"
        df = resultado.get('df', 100)
        x = np.linspace(t.ppf(0.0001, df), t.ppf(0.9999, df), 500)
        y = t.pdf(x, df)
        critical_value = t.ppf(1 - alpha/2, df)
        dist_obj = t
    else:
        dist_name = "Normal (Z)"
        df = None
        x = np.linspace(norm.ppf(0.0001), norm.ppf(0.9999), 500)
        y = norm.pdf(x)
        critical_value = norm.ppf(1 - alpha/2)
        dist_obj = norm

    ax.plot(x, y, 'b-', lw=2, label=f'Distribución H₀ ({dist_name})')
    
    # Regiones de rechazo
    x_left = np.linspace(x.min(), -critical_value, 100)
    y_left = dist_obj.pdf(x_left, df) if df else dist_obj.pdf(x_left)
    ax.fill_between(x_left, y_left, color='red', alpha=0.3, label='Región de Rechazo (α)')
    
    x_right = np.linspace(critical_value, x.max(), 100)
    y_right = dist_obj.pdf(x_right, df) if df else dist_obj.pdf(x_right)
    ax.fill_between(x_right, y_right, color='red', alpha=0.3)

    # Estadístico observado
    z_stat = resultado['statistic']
    ax.axvline(z_stat, color='green', linestyle='--', lw=2, label=f'Estadístico Obs: {z_stat:.2f}')
    
    # Anotación del p-value
    ax.annotate(f"p-value: {resultado['p_value']:.4f}", 
                xy=(z_stat, 0), xytext=(z_stat, max(y)*0.5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

    ax.set_title(f"Visualización del Test: {resultado['test_name']}")
    ax.set_xlabel("Desviaciones Estándar")
    ax.set_ylabel("Densidad de Probabilidad")
    ax.legend()
    st.pyplot(fig)

st.title("📊 Herramienta de A/B Testing")
st.caption("Una plataforma educativa y profesional para el análisis de experimentos.")

tab_calculadora, tab_sd, tab_biblioteca = st.tabs([
    "🧮 Calculadora de A/B Test", 
    "📐 Calculadora de Desviación Estándar",
    "📚 Biblioteca Teórica"
])

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
            
            # Gráfico explicativo
            plot_test_results(resultado, alpha)
                
        except ValueError as e:
            st.error(f"⚠️ Error en los datos: {e}")
        except Exception as e:
            st.error(f"🚨 Error inesperado: {e}")


# ==========================================
# PESTAÑA 2: CALCULADORA DE DESVIACIÓN ESTÁNDAR
# ==========================================
with tab_sd:
    st.header("📐 Calculadora de Desviación Estándar")
    st.write("Obtén los parámetros necesarios para tu A/B Test a partir de datos crudos o proporciones.")

    tipo_metrica = st.radio("Tipo de Métrica", ["Binomial (Proporciones)", "Continua (Medias)"], horizontal=True)

    if tipo_metrica == "Binomial (Proporciones)":
        col1, col2 = st.columns([1, 1.5])
        with col1:
            p = st.number_input("Proporción / Tasa (ej: 0.15)", min_value=0.0, max_value=1.0, value=0.15, step=0.01)
            sd_binom = np.sqrt(p * (1 - p))
            st.metric("Desviación Estándar (σ)", f"{sd_binom:.4f}")
            st.info("💡 En proporciones, la desviación depende únicamente de la tasa.")
        
        with col2:
            st.subheader("Teoría Rápida")
            st.markdown(teoria_estadistica["6. Proporciones vs. Continuas (Desviación Estándar)"]["¿Por qué en proporciones solo necesitamos la tasa?"])

    else:
        opcion_media = st.selectbox("Método de entrada", ["Opción A: Datos Crudos (CSV/Excel)", "Opción B: Resumen Estadístico"])

        if opcion_media == "Opción A: Datos Crudos (CSV/Excel)":
            archivo = st.file_uploader("Carga tu archivo", type=["csv", "xlsx"])
            if archivo:
                try:
                    if archivo.name.endswith('.csv'):
                        df_raw = pd.read_csv(archivo)
                    else:
                        df_raw = pd.read_excel(archivo)
                    
                    columna = st.selectbox("Selecciona la columna con la métrica", df_raw.select_dtypes(include=[np.number]).columns)
                    
                    data = df_raw[columna].dropna()
                    mean_val = data.mean()
                    std_val = data.std()
                    n_val = len(data)

                    m1, m2, m3 = st.columns(3)
                    m1.metric("Media ($\mu$)", f"{mean_val:.4f}")
                    m2.metric("Desv. Estándar ($s$)", f"{std_val:.4f}")
                    m3.metric("Tamaño Muestra ($n$)", n_val)
                    
                    st.success("✅ Datos calculados correctamente. Puedes usarlos en la pestaña 'Calculadora de A/B Test'.")
                except Exception as e:
                    st.error(f"Error al procesar el archivo: {e}")
        
        else:
            c1, c2, c3 = st.columns(3)
            with c1: m_manual = st.number_input("Media", value=100.0)
            with c2: s_manual = st.number_input("Desviación Estándar", value=15.0)
            with c3: n_manual = st.number_input("n (Muestra)", value=1000)
            st.info("Ingresa los valores obtenidos de herramientas como Looker, Tableau o SQL (STDDEV).")

        with st.expander("📚 ¿Por qué necesitamos estos datos?"):
            st.markdown(teoria_estadistica["6. Proporciones vs. Continuas (Desviación Estándar)"]["¿Por qué en métricas continuas necesitamos los datos crudos?"])


# ==========================================
# PESTAÑA 3: LA BIBLIOTECA 
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