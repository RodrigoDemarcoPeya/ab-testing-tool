# 📊 Herramienta de A/B Testing

Esta es una herramienta interactiva construida en Python y Streamlit para realizar contrastes de hipótesis y validar si los resultados de los experimentos (A/B Tests) son estadísticamente significativos.

## 🛠️ Características
* **Pruebas de Proporciones (Z-Test):** Ideal para métricas de conversión (Conversion Rate, Reorder Rate).
* **Pruebas de Medias (T-Test):** El estándar estadístico para evaluar variables continuas usando la aproximación de Welch (Ticket Promedio, Delta GMV).
* **Pruebas de Medias (Z-Test):** Para muestras de tamaño gigante con desviación estándar conocida.
* **Interfaz visual:** Formularios amigables e interpretación automática de resultados (Valores P e Intervalos de Confianza).

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar la herramienta en tu computadora local:

### 1. Requisitos previos
Asegúrate de tener [Python](https://www.python.org/downloads/) instalado (versión 3.8 o superior).

### 2. Clonar o descargar el proyecto
Descarga esta carpeta en tu computadora y abre una terminal (línea de comandos) en esta ubicación.

### 3. Crear un entorno virtual (Recomendado)
Es una buena práctica crear un entorno virtual para no mezclar las dependencias de este proyecto con las de tu sistema:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate

# Activar el entorno virtual (Mac/Linux)
source venv/bin/activate

# Instalar dependencias:
pip install -r requirements.txt
```
## ▶️ Cómo ejecutar la app
``` bash
python -m streamlit run main.py
```
### Luego abrí el navegador en:
http://localhost:8501


## Estructura del proyecto
``` bash
ab-testing-tool/
│
├── main.py                # App principal (Streamlit)
├── src/                   # Lógica del modelo estadístico
├── data/                  # Datos de ejemplo
├── utils/                 # Funciones auxiliares
├── requirements.txt
└── README.md
```