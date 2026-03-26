# biblioteca.py

teoria_estadistica = {
"1. Conceptos Básicos": {
"Estadístico": """Un número calculado a partir de una muestra.

Es una medida que resume información de los datos que recolectaste (Ej: la media, la varianza o una proporción).

Es decir, tomás un subconjunto de datos (la muestra) y calculás algún valor que resuma esa información.

Ejemplos de estadísticos:
- La media (promedio) de una muestra
- La mediana
- La varianza
- La desviación estándar
""",

"Parámetro": """Un número que describe una característica de toda la población.

(Ej: altura promedio de TODOS los uruguayos).

Como no podemos medir a todos, tomamos una muestra y usamos estadísticos para estimarlo.
""",

"Varianza y Desviación Estándar": """La varianza mide qué tan dispersos están los datos respecto a su media.
Es decir, indica cuánto varían los valores entre sí. Se calcula como el promedio de las diferencias al cuadrado entre cada dato y la media, por lo que sus unidades quedan “al cuadrado”. Medida de dispersión (menos intuitiva)

La desviación estándar es la raíz cuadrada de la varianza.
Esto permite volver a la unidad original de los datos y hace más fácil interpretar el resultado: representa, en promedio, cuánto se alejan los valores de la media. Es lo mismo que la desviacion pero en unidades reales y más fácil de entender
""",

"Error Estándar": """El error estándar mide qué tan variable es la media de una muestra si repitieras el muestreo muchas veces.

Es decir, indica cuánto suele alejarse la media muestral de la media real de la población.

A diferencia de la desviación estándar (que mide dispersión de datos individuales), el error estándar mide la precisión de una estimación.

👉 En resumen:

Error estándar bajo → la media estimada es más confiable

Error estándar alto → la media puede variar bastante entre muestras

💡 Intuición:
“Si tomo muchas muestras, el error estándar me dice qué tanto cambiaría la media entre una y otra”
"""
},

"2. Pruebas de Hipótesis": {
"Hipótesis Nula (H₀)": """La hipótesis nula es una afirmación inicial que se asume verdadera y que establece que no existe efecto, diferencia o relación entre las variables analizadas.

Es el punto de referencia contra el cual se comparan los datos, y el objetivo del análisis estadístico es evaluar si hay suficiente evidencia para rechazarla.

👉 En resumen:

Representa “no pasa nada” (no hay cambio o efecto)

Se asume verdadera al inicio

Se pone a prueba con los datos para ver si puede rechazarse

💡 Intuición:
“La hipótesis nula es lo que intentamos refutar con evidencia”
""",

"Hipótesis Alternativa (Hₐ)": """La hipótesis alternativa es la afirmación que plantea que sí existe un efecto, una diferencia o una relación entre las variables.

Es la hipótesis que se considera válida si hay suficiente evidencia para rechazar la hipótesis nula (H₀).

👉 En resumen:

Representa “sí pasa algo” (hay cambio o efecto)

Es la opuesta a la hipótesis nula

Se acepta solo si los datos permiten rechazar H₀
""",

"Z-Score": """El z-score indica cuántas desviaciones estándar se encuentra un valor observado respecto a la media esperada bajo la hipótesis nula.

Se utiliza para medir qué tan “extremo” es un resultado en comparación con lo que se esperaría si no hubiera efecto.

👉 En resumen:

z cercano a 0 → el valor es esperable bajo H₀

z grande (positivo o negativo) → el valor es poco probable bajo H₀

💡 Intuición:
“Cuanto más lejos esté el resultado de lo esperado (en términos de desviaciones estándar), más evidencia hay contra la hipótesis nula”

👉 Por eso:
Un z-score alto (en valor absoluto) indica mayor evidencia para rechazar H₀
""",
"P-Value": """El p-value es la probabilidad de obtener un resultado igual o más extremo que el observado, asumiendo que la hipótesis nula (H₀) es verdadera.

Se usa para medir qué tan compatible son los datos con H₀.

👉 En resumen:

p-value alto → los datos son consistentes con H₀

p-value bajo → los datos son poco probables bajo H₀

💡 Intuición:
“Si H₀ fuera cierta, ¿qué tan raro es lo que observé?”

👉 Regla práctica:

p < 0.05 → se suele rechazar H₀

p ≥ 0.05 → no hay evidencia suficiente para rechazar H₀
"""
,         

"Significancia Estadística (α)": """La significancia estadística (α) es el umbral que define qué tan improbable debe ser un resultado para rechazar la hipótesis nula (H₀).

Representa el nivel máximo de error que estás dispuesto a aceptar al rechazar H₀ cuando en realidad es verdadera (error tipo I).

👉 En resumen:

α define el criterio de decisión

Es el punto de corte para comparar con el p-value

💡 Regla práctica:

Si p-value < α → se rechaza H₀

Si p-value ≥ α → no se rechaza H₀

💡 Intuición:
“α es el nivel de ‘exigencia’ que ponés para considerar un resultado como suficientemente raro”

👉 Ejemplo común:

α = 0.05 → aceptás un 5% de riesgo de rechazar H₀ por error
"""
},

"3. Errores, Potencia y MDE": {
"Error Tipo 1 (α) (Falso Positivo)": """Rechazamos H₀ cuando en realidad es verdadera.

Concluimos que hay un efecto o diferencia, pero en realidad todo se debe al azar.

👉 Ejemplo:
Pensás que un cambio en la web mejoró la conversión, pero en realidad no cambió nada.
""",

"Error Tipo 2 (β)(Falso Negativo)": """No rechazamos H₀ cuando en realidad es falsa.

Concluimos que no hay efecto, pero en realidad sí lo hay y no lo detectamos.

👉 Ejemplo:
El nuevo botón sí mejora la conversión, pero los datos no fueron suficientes para detectarlo.
""",        
"Potencia de la prueba (1-β)": """La potencia de la prueba es la probabilidad de rechazar correctamente la hipótesis nula (H₀) cuando es falsa.

Es decir, mide qué tan capaz es el test de detectar un efecto real cuando realmente existe.

👉 En resumen:

Alta potencia → mayor probabilidad de detectar efectos reales

Baja potencia → mayor riesgo de cometer un error tipo II (no detectar el efecto)

💡 Intuición:
“Si realmente hay un cambio, la potencia indica qué tan probable es que lo encuentres”

👉 Relación clave:

Potencia = 1 − β

β = probabilidad de error tipo II
""",

"MDE (Mínimo Efecto Detectable)": """El MDE es el cambio más pequeño que una prueba puede detectar como estadísticamente significativo, dado un nivel de significancia (α) y una potencia (1 − β).

Define el umbral mínimo de efecto que el experimento está preparado para identificar con confianza.
👉 En resumen:

Es el “mínimo cambio detectable”

Depende del tamaño de muestra, α y la potencia

Efectos más pequeños que el MDE probablemente no se detecten

💡 Intuición:
“El MDE te dice qué tan ‘fino’ es tu experimento para detectar cambios”

👉 Ejemplo:
Si el MDE es 5% → solo vas a detectar cambios de 5% o más como significativos; cambios menores pueden pasar desapercibidos.

La diferencia es lo suficientemente grande como para ser estadísticamente significativa (p < α)
"""
},

"4. Métodos de Experimentación": {
"Fixed Sample (Frecuentista)": """Es el método tradicional de experimentación.

Consiste en definir de antemano un tamaño de muestra fijo, recolectar datos hasta alcanzarlo y analizar los resultados una sola vez al final.

👉 En resumen:

Se fija el tamaño de muestra antes de empezar

No se deben mirar resultados intermedios

La decisión se toma al finalizar el experimento

💡 Intuición:
“Primero juntás todos los datos, después decidís”

📌 Importante:
Mirar los resultados antes de tiempo puede aumentar el riesgo de errores (falsos positivos), por eso el análisis se hace solo al final.
""",

"Sequential (Frecuentista)": """Es un método que permite analizar los datos en distintos momentos durante el experimento, sin necesidad de esperar al tamaño de muestra final.

Si en alguno de esos puntos se alcanza evidencia suficiente, el experimento puede detenerse antes de tiempo.

👉 En resumen:

Se permiten análisis intermedios

El experimento puede terminar anticipadamente

Requiere ajustar los criterios estadísticos para evitar errores

💡 Intuición:
“Vas mirando los resultados a medida que llegan y podés cortar antes si ya es concluyente”
""",

"Bayesiano": """Es un enfoque de experimentación que utiliza probabilidades para estimar directamente qué tan probable es que una variante sea mejor que otra.

En lugar de basarse en rechazar o no una hipótesis, calcula la probabilidad de que una opción supere a la otra dado los datos observados.

👉 En resumen:

Usa distribuciones de probabilidad

No trabaja con p-values ni rechazo de H₀

Entrega resultados en términos de probabilidades directas

💡 Intuición:
“¿Qué tan probable es que B sea mejor que A?”
"""
    },
    "5. Modalidades de análisis": {
        "Proporciones": """x
""",

        "Medias (T - Test)": """x”
""",

        "Z Test": """x
"""
}

}