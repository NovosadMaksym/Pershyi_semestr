import logging


def run_logging_demo():
    # Налаштування базового логера
    logger = logging.getLogger("PracticalLogger")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        logger.addHandler(ch)

    logger.info("Виклик тестового логу в середині функції.")
    return "[logging] Компонент логування успішно ініціалізовано."
