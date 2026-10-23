from data import RECIPES
from inventory import add_potion

def can_craft(recipe, ingredients_inventory):
    try:
        for item, needed in recipe.items():
            if ingredients_inventory.get(item, 0) < needed:
                return False
        return True
    except Exception:
        return False

def get_available_potions(ingredients_inventory):
    available = []
    try:
        for potion, recipe in RECIPES.items():
            if can_craft(recipe, ingredients_inventory):
                available.append(potion)
    except Exception as e:
        print(f"Помилка пошуку доступних зілль: {e}")
    return available

def craft_potion(potion_name, amount, ingredients_inventory, potions_inventory):
    try:
        recipe = RECIPES[potion_name]

        for item, needed in recipe.items():
            if ingredients_inventory.get(item, 0) < needed * amount:
                print(f"Не вистачає: {item}")
                return False

        for item, needed in recipe.items():
            ingredients_inventory[item] -= needed * amount
            if ingredients_inventory[item] <= 0:
                del ingredients_inventory[item]

        added = add_potion(potions_inventory, potion_name, amount)
        if added < amount:
            print("Не вистачило місця в інвентарі зілль!")
        else:
            print(f"Зварено {amount} × «{potion_name}»")
        return True
    except Exception as e:
        print(f"Помилка крафту: {e}")
        return False

def craft_menu(ingredients_inventory, potions_inventory):
    while True:
        print("\n===== КРАФТ =====")
        available = get_available_potions(ingredients_inventory)

        if not available:
            print("Немає доступних рецептів.")
            print("0. Назад")
            if input("Вибір: ").strip() == "0":
                break
            continue

        for i, p in enumerate(available, 1):
            print(f"{i}. {p}")
        print("0. Назад")

        try:
            choice = input("Номер зілля: ").strip()
            if choice == "0":
                break
            idx = int(choice) - 1
            if not (0 <= idx < len(available)):
                print("Невірний номер")
                continue

            potion = available[idx]
            amount = int(input(f"Скільки варити «{potion}»? "))
            if amount > 0:
                craft_potion(potion, amount, ingredients_inventory, potions_inventory)
        except ValueError:
            print("Вводьте числа")
        except Exception as e:
            print(f"Помилка: {e}")