import math

def run_math_demo():
    # Розрахунок гіпотенузи та округлення вгору
    hypotenuse = math.hypot(3, 4)
    rounded = math.ceil(5.1)
    return f"[math] Гіпотенуза трикутника (3, 4) = {hypotenuse}, math.ceil(5.1) = {rounded}"
