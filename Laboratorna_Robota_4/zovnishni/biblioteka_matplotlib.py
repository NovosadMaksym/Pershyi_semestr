import matplotlib.pyplot as plt


def run_matplotlib_demo():
    # Генерація графіка та збереження в папку output
    plt.figure(figsize=(4, 2))
    plt.plot([1, 2, 3], [10, 40, 90], color='green', marker='x')
    plt.title("Matplotlib Result")

    path = "output/chart_matplotlib.png"
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    return f"[matplotlib] Графік збережено за шляхом: {path}"
