import time

def run_time_demo():
    # Отримання поточної позначки часу
    current_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return f"[time] Поточний системний час: {current_stamp}"
