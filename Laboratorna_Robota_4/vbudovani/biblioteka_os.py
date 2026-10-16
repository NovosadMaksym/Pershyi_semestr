import os

def run_os_demo():
    # Створюємо папку для результатів роботи програми
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return f"[os] Створено або перевірено директорію: {os.path.abspath(output_dir)}"
