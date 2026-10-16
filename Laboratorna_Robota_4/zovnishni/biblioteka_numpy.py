import numpy as np

def run_numpy_demo():
    # Створення масиву випадкових оцінок та розрахунок медіани
    grades = np.array([90, 85, 100, 75, 95])
    return f"[numpy] Масив оцінок: {grades}. Медіанне значення: {np.median(grades)}"
