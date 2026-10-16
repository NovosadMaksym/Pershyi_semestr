import json

def run_json_demo():
    # Конвертуємо словник у рядок формату JSON
    student_data = {"name": "Олександр", "task": "Practical 1", "completed": True}
    json_string = json.dumps(student_data, indent=2)
    return f"[json] Результат серіалізації структури даних:\n{json_string}"
