import numpy as np
from scipy.stats import norm, t

class HypothesisTester:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def _validate_inputs(self, n_a, n_b, std_a=None, std_b=None):
        """Valida que los tamaños de muestra y desviaciones sean válidos."""
        if n_a <= 0 or n_b <= 0:
            raise ValueError("El tamaño de muestra (N) debe ser mayor a 0.")
        if std_a is not None and (std_a < 0 or std_b < 0):
            raise ValueError("La desviación estándar no puede ser negativa.")

    def z_test_proportions(self, prop_a, prop_b, n_a, n_b):
        """Modalidad 1: Contraste de proporciones (Ej: Conversion Rate)"""
        self._validate_inputs(n_a, n_b)
        
        p_pool = (prop_a * n_a + prop_b * n_b) / (n_a + n_b)
        
        # Evitar división por cero si p_pool es 0 o 1
        if p_pool == 0 or p_pool == 1:
            return self._format_results("Z-Test (Proporciones)", 0, 1.0, prop_b - prop_a)
            
        se = np.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))
        z_stat = (prop_b - prop_a) / se
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
        
        return self._format_results("Z-Test (Proporciones)", z_stat, p_value, prop_b - prop_a)

    def z_test_means(self, mean_a, mean_b, std_a, std_b, n_a, n_b):
        """Modalidad 2: Contraste Z de medias (Para muestras gigantes)"""
        self._validate_inputs(n_a, n_b, std_a, std_b)
        
        se = np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
        if se == 0:
            return self._format_results("Z-Test (Medias)", 0, 1.0, mean_b - mean_a)
            
        z_stat = (mean_b - mean_a) / se
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
        
        return self._format_results("Z-Test (Medias)", z_stat, p_value, mean_b - mean_a)

    def t_test_means(self, mean_a, mean_b, std_a, std_b, n_a, n_b):
        """Modalidad 3: Contraste T de medias (Welch's T-test)"""
        self._validate_inputs(n_a, n_b, std_a, std_b)
        
        var_a = std_a**2
        var_b = std_b**2
        
        se = np.sqrt((var_a / n_a) + (var_b / n_b))
        if se == 0:
            return self._format_results("T-Test (Medias de Welch)", 0, 1.0, mean_b - mean_a)
            
        t_stat = (mean_b - mean_a) / se
        
        # Grados de libertad (Welch–Satterthwaite)
        df_num = (var_a / n_a + var_b / n_b)**2
        df_den = ((var_a / n_a)**2 / (n_a - 1)) + ((var_b / n_b)**2 / (n_b - 1))
        df = df_num / df_den
        
        p_value = 2 * (1 - t.cdf(abs(t_stat), df))
        
        return self._format_results("T-Test (Medias de Welch)", t_stat, p_value, mean_b - mean_a)

    def _format_results(self, test_name, statistic, p_value, diff):
        """Centraliza el formato de salida."""
        return {
            "test_name": test_name,
            "statistic": float(statistic),
            "p_value": float(p_value),
            "diff": float(diff),
            "is_significant": bool(p_value < self.alpha),
            "alpha": self.alpha
        }