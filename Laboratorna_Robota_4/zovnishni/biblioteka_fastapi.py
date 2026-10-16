import fastapi

def run_fastapi_demo():
    # Тест декларації екземпляра сервера FastAPI
    app = fastapi.FastAPI(title="Demo API")
    return f"[fastapi] Модуль підключено. Зареєстровано додаток: '{app.title}' (v{fastapi.__version__})"
