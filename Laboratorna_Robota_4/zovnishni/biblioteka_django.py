import django
from django.conf import settings

def run_django_demo():
    # Ініціалізація мінімального середовища ядра Django
    if not settings.configured:
        settings.configure(DEBUG=True, SECRET_KEY='secret')
    django.setup()
    return f"[django] Архітектурне середовище Django успішно запущено (v{django.get_version()})"
