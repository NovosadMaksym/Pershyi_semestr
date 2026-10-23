import random
from data import INGREDIENTS, DAILY_INGREDIENTS, WIN_GOLD, MAX_DAYS
from inventory import add_ingredient


def give_daily_ingredients(ingredients_inventory):
    """
    Видає DAILY_INGREDIENTS інгредієнтів.
    Якщо стак повний — шукає інший інгредієнт, який можна покласти.
    """
    try:
        added_count = 0
        attempts = 0
        max_attempts = DAILY_INGREDIENTS * 100  # захист від нескінченного циклу

        while added_count < DAILY_INGREDIENTS and attempts < max_attempts:
            attempts += 1

            # Вибираємо випадковий інгредієнт
            ing = random.choice(INGREDIENTS)

            # Пробуємо додати
            added = add_ingredient(ingredients_inventory, ing, 1)

            if added > 0:
                added_count += 1
            # якщо не вдалося — просто пробуємо наступний

        if added_count > 0:
            print(f"Отримано {added_count} інгредієнтів на новий день.")
        else:
            print("Інвентар повністю заповнений! Нові інгредієнти не отримано.")

    except Exception as e:
        print(f"Помилка видачі інгредієнтів: {e}")


def check_game_end(gold, day):
    try:
        if gold >= WIN_GOLD:
            print(f"\n*** ПЕРЕМОГА! Ти накопичив {gold} золота! ***")
            return True
        if day > MAX_DAYS:
            print(f"\n*** ПРОГРАШ! Минуло {MAX_DAYS} днів. ***")
            return True
        return False
    except Exception as e:
        print(f"Помилка перевірки кінця гри: {e}")
        return False