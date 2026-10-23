from data import MAX_STACK_ING, MAX_STACK_POT, MAX_INGREDIENT_SLOTS, MAX_POTION_SLOTS

def show_inventory(ingredients_inventory, potions_inventory):
    try:
        print("\n===== ІНВЕНТАР =====")
        print("\n--- Інгредієнти ---")
        if ingredients_inventory:
            for item, amount in ingredients_inventory.items():
                print(f"  {item}: {amount}")
        else:
            print("  Порожньо")

        print("\n--- Зілля ---")
        if potions_inventory:
            for item, amount in potions_inventory.items():
                print(f"  {item}: {amount}")
        else:
            print("  Порожньо")
    except Exception as e:
        print(f"Помилка показу інвентаря: {e}")

def add_ingredient(inventory, name, amount=1):
    try:
        if len(inventory) >= MAX_INGREDIENT_SLOTS and name not in inventory:
            return 0
        current = inventory.get(name, 0)
        can_add = min(amount, MAX_STACK_ING - current)
        if can_add <= 0:
            return 0
        inventory[name] = current + can_add
        return can_add
    except Exception as e:
        print(f"Помилка додавання інгредієнта: {e}")
        return 0

def add_potion(inventory, name, amount=1):
    try:
        if len(inventory) >= MAX_POTION_SLOTS and name not in inventory:
            return 0
        current = inventory.get(name, 0)
        can_add = min(amount, MAX_STACK_POT - current)
        if can_add <= 0:
            return 0
        inventory[name] = current + can_add
        return can_add
    except Exception as e:
        print(f"Помилка додавання зілля: {e}")
        return 0