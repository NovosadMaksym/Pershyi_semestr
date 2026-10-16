import pandas as pd

def run_pandas_demo():
    # Створення об'єкта DataFrame
    df = pd.DataFrame({"Предмет": ["Програмування", "Мат. аналіз"], "Оцінка": [95, 88]})
    return f"[pandas] Згенеровано звітну матрицю DataFrame:\n{df.to_string()}"
