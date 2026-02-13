# Modulo educativo: explicaciones.py

def obtener_explicacion(modalidad):
    """
    Recibe el nombre de la modalidad seleccionada y devuelve un diccionario
    con su título, cómo funciona matemáticamente y cuándo es apropiado usarla.
    """
    diccionario_explicaciones = {
        "Proporciones": {
            "titulo": "Prueba Z para Proporciones",
            "como_funciona": "Compara la tasa de éxito (proporción) entre dos grupos. Utiliza una aproximación de la distribución normal para calcular qué tan lejos está la diferencia observada respecto a lo que esperaríamos si fuera mero azar.",
            "cuando_usar": "✅ IDEAL PARA: Variables categóricas o binarias (Sí/No, Éxito/Fracaso).\n\nEjemplos clásicos:\n- Tasa de Conversión (compró o no compró)\n- Click-Through Rate / CTR (hizo clic o no)\n- Tasa de Retención (volvió o no volvió)"
        },
        "T-Test": {
            "titulo": "Prueba T de Student (Aproximación de Welch)",
            "como_funciona": "Compara los promedios aritméticos de dos grupos. A diferencia del Z-Test, penaliza estadísticamente el hecho de que solo tenemos la desviación estándar de nuestra muestra empírica y no la de toda la población. La variante 'Welch' asume inteligentemente que las varianzas de los dos grupos son diferentes.",
            "cuando_usar": "✅ IDEAL PARA: Variables continuas numéricas. ES EL ESTÁNDAR DE LA INDUSTRIA.\n\nEjemplos clásicos:\n- Ticket Promedio (AOV)\n- Revenue por Usuario (ARPU)\n- Tiempo en pantalla (segundos)\n- Frecuencia de compra (Deltas)"
        },
        "Z-Test (Gigantes)": {
            "titulo": "Prueba Z para Medias",
            "como_funciona": "Matemáticamente similar al T-Test, pero asume que conocemos la desviación estándar poblacional exacta o que la muestra es tan infinitamente grande que la distribución es perfectamente normal.",
            "cuando_usar": "⚠️ CASOS DE USO RESTRINGIDOS:\n\nSolo úsalo cuando analices muestras verdaderamente gigantescas (ej. cientos de miles de eventos) donde el Z-Test y el T-Test arrojan resultados casi idénticos. En la vida real empresarial, el T-Test es siempre más seguro y preferido."
        }
    }

    # Buscar la clave correcta según lo que diga el combobox
    for clave, contenido in diccionario_explicaciones.items():
        if clave in modalidad:
            return contenido
            
    return None