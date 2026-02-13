import numpy as np
from scipy.stats import norm, t

class HypothesisTester:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def z_test_proportions(self, prop_a, prop_b, n_a, n_b):
        """Modalidad 1: Contraste de proporciones (Ej: Conversion Rate)"""
        p_pool = (prop_a * n_a + prop_b * n_b) / (n_a + n_b)
        se = np.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))
        
        z_stat = (prop_b - prop_a) / se
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
        
        diff = prop_b - prop_a
        return self._format_results("Z-Test (Proporciones)", z_stat, p_value, diff)

    def z_test_means(self, mean_a, mean_b, std_a, std_b, n_a, n_b):
        """Modalidad 2: Contraste Z de medias (Para muestras gigantes)"""
        se = np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
        z_stat = (mean_b - mean_a) / se
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
        
        diff = mean_b - mean_a
        return self._format_results("Z-Test (Medias)", z_stat, p_value, diff)

    def t_test_means(self, mean_a, mean_b, std_a, std_b, n_a, n_b):
        """Modalidad 3: Contraste T de medias (El estándar para variables continuas)"""
        # Error estándar
        se = np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
        t_stat = (mean_b - mean_a) / se
        
        # Grados de libertad (Aproximación de Welch)
        df_num = ((std_a**2 / n_a) + (std_b**2 / n_b))**2
        df_den = ((std_a**2 / n_a)**2 / (n_a - 1)) + ((std_b**2 / n_b)**2 / (n_b - 1))
        df = df_num / df_den
        
        # Valor p usando la distribución T
        p_value = 2 * (1 - t.cdf(abs(t_stat), df))
        
        diff = mean_b - mean_a
        return self._format_results("T-Test (Medias de Welch)", t_stat, p_value, diff)

    def _format_results(self, test_name, statistic, p_value, diff):
        """Formatea la salida para que la interfaz gráfica la lea fácil"""
        is_significant = p_value < self.alpha
        return {
            "test_name": test_name,
            "statistic": statistic,
            "p_value": p_value,
            "diff": diff,
            "is_significant": is_significant,
            "alpha": self.alpha
        }