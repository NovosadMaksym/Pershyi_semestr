# Імпорт функцій з вбудованих модулів
from vbudovani.biblioteka_os import run_os_demo
from vbudovani.biblioteka_json import run_json_demo
from vbudovani.biblioteka_math import run_math_demo
from vbudovani.biblioteka_time import run_time_demo
from vbudovani.biblioteka_logging import run_logging_demo

# Імпорт функцій із зовнішніх модулів
from zovnishni.biblioteka_requests import run_requests_demo
from zovnishni.biblioteka_pandas import run_pandas_demo
from zovnishni.biblioteka_numpy import run_numpy_demo
from zovnishni.biblioteka_matplotlib import run_matplotlib_demo
from zovnishni.biblioteka_seaborn import run_seaborn_demo
from zovnishni.biblioteka_bs4 import run_bs4_demo
from zovnishni.biblioteka_pydantic import run_pydantic_demo
from zovnishni.biblioteka_pillow import run_pillow_demo
from zovnishni.biblioteka_fastapi import run_fastapi_demo
from zovnishni.biblioteka_django import run_django_demo


def main():
    print("==================================================")
    print("   ЗАПУСК ПРАКТИЧНОЇ РОБОТИ: МОДУЛЬНА СТРУКТУРА   ")
    print("==================================================\n")

    # 1. Запуск вбудованих бібліотек
    print("--- [ВБУДОВАНІ БІБЛІОТЕКИ] ---")
    print(run_os_demo())
    print(run_json_demo())
    print(run_math_demo())
    print(run_time_demo())
    print(run_logging_demo())
    print()

    # 2. Запуск зовнішніх бібліотек
    print("--- [ЗОВНІШНІ БІБЛІОТЕКИ] ---")
    print(run_requests_demo())
    print(run_pandas_demo())
    print(run_numpy_demo())
    print(run_matplotlib_demo())
    print(run_seaborn_demo())
    print(run_bs4_demo())
    print(run_pydantic_demo())
    print(run_pillow_demo())
    print(run_fastapi_demo())
    print(run_django_demo())

    print("\n==================================================")
    print("   УСІ МОДУЛІ УСПІШНО ВИКОНАЛИ СВОЇ ФУНКЦІЇ!    ")
    print("==================================================")


if __name__ == "__main__":
    main()
