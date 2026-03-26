# 📊 Gemini Context: A/B Testing & Statistical Learning Tool

This project is an interactive tool built with **Python** and **Streamlit** designed for performing real-world A/B tests and serving as an educational platform for statistical concepts.

## 🚀 Project Overview

- **Main Technologies:** Python, Streamlit, SciPy, NumPy.
- **Architecture:** 
    - `main.py`: Entry point and UI definitions using Streamlit.
    - `stats_engine.py`: Core logic for statistical tests (Z-tests for proportions/means and Welch's T-test).
    - `biblioteca.py`: Data structure containing a comprehensive dictionary of statistical concepts.
    - `explicaciones.py`: Mapping between analysis modes and educational content.

## 🛠 Building and Running

### Prerequisites
- Python 3.9+
- A virtual environment is recommended.

### Commands
- **Install Dependencies:** `pip install -r requirements.txt`
- **Run the Application:** `python -m streamlit run main.py`
- **Tests:** (TODO: No automated tests found in the repository. Statistical logic is in `stats_engine.py`).

## 📖 Development Conventions

- **Frontend:** Streamlit is used for the UI. Layout is centered by default.
- **Statistical Logic:** Encapsulated in the `HypothesisTester` class within `stats_engine.py`. Results are returned as a standard dictionary for easy UI consumption.
- **Content Separation:** Theoretical definitions and educational explanations are stored in separate files (`biblioteca.py`, `explicaciones.py`) to keep the UI logic clean.
- **Language:** The UI and documentation are in **Spanish**, while the code (variables, classes, methods) follows **English** naming conventions.

## 📂 Key Files

- `main.py`: Orchestrates the Streamlit tabs and handles user inputs/outputs.
- `stats_engine.py`: Implements `HypothesisTester` with `z_test_proportions`, `z_test_means`, and `t_test_means`.
- `biblioteca.py`: Contains `teoria_estadistica`, a nested dictionary of concepts used in the "Biblioteca Teórica" tab.
- `explicaciones.py`: Contains `obtener_explicacion`, providing contextual help for the selected analysis mode.
