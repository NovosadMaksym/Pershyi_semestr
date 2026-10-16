import requests

def run_requests_demo():
    # Перевірка доступності веб-сервера
    response = requests.get("https://github.com", timeout=5)
    return f"[requests] Запит до GitHub API повернув статус: {response.status_code}"
