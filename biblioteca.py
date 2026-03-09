# biblioteca.py

teoria_estadistica = {
    "1. Conceptos Básicos": {
        "Estadístico": "Un número calculado a partir de una muestra. Es una medida que resume información de los datos que recolectaste (Ej: la media, la varianza o una proporción de tu muestra).",
        "Parámetro": "Un número que describe una característica de toda la población (Ej: altura promedio de TODOS los uruguayos). Como no podemos medir a todos, tomamos una muestra y usamos estadísticos para estimarlo.",
        "Varianza y Desviación Estándar": "La varianza indica qué tan dispersos están los datos respecto a su media (en unidades al cuadrado). La Desviación Estándar es su raíz cuadrada y vuelve a la unidad original, indicando cuánto se alejan en promedio los valores respecto a la media.",
        "Error Estándar": "Medida de la variabilidad de la media de la muestra. Te indica cuánto es probable que la media de tu muestra se aleje de la media real poblacional. Un error más bajo significa mayor precisión."
    },
    "2. Pruebas de Hipótesis": {
        "Hipótesis Nula (H₀)": "Es el punto de partida. Se asume verdadera al inicio y representa que 'no hay efecto' o 'no hay diferencia'. Es la que sometemos a prueba.",
        "Hipótesis Alternativa (Hₐ)": "Es lo que realmente queremos demostrar. Representa que sí hay efecto, que sí hay diferencia o que algo cambió.",
        "Z-Score": "Mide cuántas desviaciones estándar se encuentra un valor de la media esperada bajo la hipótesis nula. Un z-score mayor (en valor absoluto) indica mayor probabilidad de rechazar la hipótesis nula.",
        "Significancia Estadística (α)": "Indica cuán rara debe ser la diferencia respecto a H₀ para rechazarla. El hecho de rechazar H₀ significa que los datos brindan suficiente evidencia de que es estadísticamente improbable que el cambio sea por azar."
    },
    "3. Errores, Potencia y MDE": {
        "Error Tipo 1 (Falso Positivo)": "Rechazamos H₀ cuando en realidad es verdadera. Creemos que hay diferencia, cambio o efecto, pero en realidad NO lo hay.",
        "Error Tipo 2 (Falso Negativo)": "No rechazamos H₀ cuando en realidad es falsa. Creemos que no hay diferencia, pero en realidad SÍ la hay (se designa con β).",
        "Potencia de la prueba (1-β)": "La probabilidad de rechazar correctamente H₀ cuando es falsa. Mide qué tan buena es la prueba para detectar un efecto cuando realmente existe.",
        "MDE (Mínimo Efecto Detectable)": "Es el tamaño del efecto más pequeño que nuestra prueba puede detectar como estadísticamente significativo."
    },
    "4. Métodos de Experimentación": {
        "Fixed Sample (Frecuentista)": "Método tradicional. Se define un tamaño de muestra fijo antes de iniciar, se recolectan los datos hasta alcanzarlo y luego se analiza.",
        "Sequential (Frecuentista)": "Permite realizar análisis en puntos intermedios. Si muestra diferencia significativa antes de alcanzar la muestra completa, el experimento puede detenerse.",
        "Bayesiano": "Usa distribuciones de probabilidad para calcular si una variación es mejor, proporcionando una interpretación en términos de 'probabilidad de ganar'."
    }
}