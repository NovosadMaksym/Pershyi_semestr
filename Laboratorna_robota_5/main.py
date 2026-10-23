from inventory import show_inventory
from craft import craft_menu
from utils import give_daily_ingredients, check_game_end
from data import START_GOLD, PRICES

ingredients_inventory = {}
potions_inventory = {}
gold = START_GOLD
day = 1

def show_menu():
    print(f"\n===== День {day} =====")
    print(f"Золото: {gold}")
    print("1. Інвентар")
    print("2. Крафт зілля")
    print("3. Закінчити день (продаж цілля + нові інгредієнти)")
    print("0. Вийти")

def sell_potions():
    global gold
    try:
        if not potions_inventory:
            print("Немає зілль для продажу.")
            return

        print("\n===== ПРОДАЖ =====")
        total = 0
        for potion, amount in list(potions_inventory.items()):
            price = PRICES.get(potion, 10)
            money = price * amount
            print(f"{potion} × {amount} = {money} золота")
            total += money
            del potions_inventory[potion]

        gold += total
        print(f"Продано все на {total} золота. Тепер у тебе {gold}.")
    except Exception as e:
        print(f"Помилка продажу: {e}")

def start_game():
    global day, gold

    while True:
        if check_game_end(gold, day):
            return

        give_daily_ingredients(ingredients_inventory)

        while True:
            show_menu()
            try:
                choice = input("Вибір: ").strip()

                if choice == "1":
                    show_inventory(ingredients_inventory, potions_inventory)
                elif choice == "2":
                    craft_menu(ingredients_inventory, potions_inventory)
                elif choice == "3":
                    sell_potions()
                    break
                elif choice == "0":
                    print("Гру завершено.")
                    return
                else:
                    print("Невірний вибір")
            except Exception as e:
                print(f"Помилка: {e}")

        day += 1

if __name__ == "__main__":
    start_game()