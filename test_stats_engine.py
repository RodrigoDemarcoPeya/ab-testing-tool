import pytest
import numpy as np
from stats_engine import HypothesisTester

def test_z_test_proportions():
    tester = HypothesisTester(alpha=0.05)
    # Proporciones: 10% vs 12% con n=1000 cada uno
    res = tester.z_test_proportions(0.10, 0.12, 1000, 1000)
    
    assert res["test_name"] == "Z-Test (Proporciones)"
    assert res["statistic"] == pytest.approx(1.429, abs=1e-3)
    assert res["p_value"] == pytest.approx(0.153, abs=1e-3)
    assert res["is_significant"] is False
    assert res["diff"] == pytest.approx(0.02)

def test_z_test_proportions_significant():
    tester = HypothesisTester(alpha=0.05)
    # Proporciones: 10% vs 15% con n=1000 cada uno (Debe ser significativo)
    res = tester.z_test_proportions(0.10, 0.15, 1000, 1000)
    assert res["is_significant"] is True
    assert res["p_value"] < 0.05

def test_z_test_means():
    tester = HypothesisTester(alpha=0.05)
    # Medias: 100 vs 110, std=15, n=100
    res = tester.z_test_means(100, 110, 15, 15, 100, 100)
    
    assert res["test_name"] == "Z-Test (Medias)"
    assert round(res["statistic"], 3) == 4.714
    assert res["p_value"] < 0.001
    assert res["is_significant"] is True
    assert res["diff"] == 10.0

def test_t_test_means_welch():
    tester = HypothesisTester(alpha=0.05)
    # Medias: 10 vs 12, std_a=2, std_b=5, n=30
    res = tester.t_test_means(10, 12, 2, 5, 30, 30)
    
    assert res["test_name"] == "T-Test (Medias de Welch)"
    assert round(res["statistic"], 3) == 2.034
    assert round(res["p_value"], 3) == 0.049  # Approx based on df ~38
    assert res["is_significant"] is True
    assert res["diff"] == 2.0

def test_validation_errors():
    tester = HypothesisTester()
    with pytest.raises(ValueError, match="El tamaño de muestra"):
        tester.z_test_proportions(0.1, 0.2, 0, 100)
    
    with pytest.raises(ValueError, match="La desviación estándar no puede ser negativa"):
        tester.z_test_means(10, 12, -1, 5, 100, 100)

def test_edge_case_zero_diff():
    tester = HypothesisTester()
    res = tester.z_test_proportions(0.1, 0.1, 100, 100)
    assert res["statistic"] == 0
    assert res["p_value"] == 1.0
    assert res["diff"] == 0
    assert res["is_significant"] is False

def test_edge_case_zero_variance():
    tester = HypothesisTester()
    # Si std es 0 y medias son iguales
    res = tester.t_test_means(10, 10, 0, 0, 10, 10)
    assert res["statistic"] == 0
    assert res["p_value"] == 1.0
