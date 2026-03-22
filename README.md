# 📊 Herramienta de A/B Testing & Aprendizaje Estadístico

Esta es una herramienta interactiva construida en **Python** y **Streamlit** diseñada con un doble propósito:
1. **Realizar contrastes de hipótesis reales** para validar si los resultados de los experimentos (A/B Tests) son estadísticamente significativos.
2. **Servir como plataforma educativa** para aprender e interiorizar conceptos estadísticos aplicados al mundo del producto y la experimentación.

## 🛠️ Características Principales

La aplicación se divide en dos secciones (pestañas) principales:

### 🧮 1. Calculadora de A/B Test
Una interfaz visual para ejecutar pruebas estadísticas clave:
* **Pruebas de Proporciones (Z-Test):** Ideal para métricas de conversión (Conversion Rate, Reorder Rate, CTR, etc.).
* **Pruebas de Medias (T-Test):** El estándar estadístico para evaluar variables continuas usando la aproximación de Welch (Ticket Promedio, Tiempo en app, Revenue por usuario).
* **Pruebas de Medias Gigantes (Z-Test):** Para muestras de tamaño masivo (cientos de miles de eventos) con desviación estándar conocida.
* **Módulo Educativo Integrado:** Cada modalidad incluye explicaciones dinámicas sobre "cómo funciona matemáticamente" y "cuándo es mejor usarla".

### 📚 2. Biblioteca Teórica
Un diccionario estadístico completo basado en el conocimiento curado del proyecto para rápida consulta:
* **Conceptos Básicos:** Estadístico, Parámetro, Varianza, Error Estándar.
* **Pruebas de Hipótesis:** H₀, Hₐ, Z-Score, P-Value, Significancia (α).
* **Errores y Potencia:** Error Tipo 1 (Falso Positivo), Error Tipo 2 (Falso Negativo), Potencia (1-β), MDE (Mínimo Efecto Detectable).
* **Métodos de Experimentación:** Frecuentista (Fixed y Sequential) vs. Bayesiano.

---

## 🚀 Instalación y Uso Local

Sigue estos pasos para ejecutar la herramienta en tu computadora:

### 1. Requisitos Previos
Asegúrate de tener [Python](https://www.python.org/downloads/) instalado (se recomienda una versión reciente como 3.9 o superior).

### 2. Clonar el Proyecto
Clona este repositorio en tu máquina local y abre una terminal en la carpeta principal del proyecto:
```bash
git clone https://github.com/RodrigoDemarcoPeya/ab-testing-tool.git
cd ab-testing-tool
```

### 3. Crear un Entorno Virtual (Recomendado)
Es una buena práctica trabajar en un entorno virtual para mantener limpias las dependencias de tu sistema.
```bash
# Crear el entorno virtual llamado 'venv'
python -m venv venv

# Activar el entorno virtual (En Windows)
venv\Scripts\activate

# Activar el entorno virtual (En Mac/Linux)
source venv/bin/activate
```

### 4. Instalar Dependencias
Una vez activo el entorno virtual, instala los paquetes requeridos (`streamlit`, `scipy`, `numpy`):
```bash
pip install -r requirements.txt
```

### 5. ▶️ Ejecutar la Aplicación
Arranca el servidor local de Streamlit con el siguiente comando:
```bash
python -m streamlit run main.py
```

La aplicación se abrirá automáticamente en tu navegador por defecto, generalmente en:
**[http://localhost:8501](http://localhost:8501)**

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```bash
ab-testing-tool/
│
├── main.py                # App principal (Frontend Streamlit)
├── stats_engine.py        # Motor estadístico (Z-Tests, T-Tests de Welch)
├── biblioteca.py          # Diccionario de conceptos y glosario
├── explicaciones.py       # Textos y lógicas del módulo educativo
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación e instrucciones
```

---

*¡Hecho para facilitar la experimentación de producto y la comprensión estadística fundamental!*