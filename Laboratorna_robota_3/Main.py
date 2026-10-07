# Константи
COMMANDS = [
    {  # 1
        "name": "Показати список команд",
        "action": "show_available_commands"
    },
    {  # 2
        "name": "Показати каталог",
        "action": "show_catalog"
    },
    {  # 3
        "name": "Показати кошик",
        "action": "show_cart"
    },
    {  # 4
        "name": "Оплатити товари в кошику",
        "action": "buy_products_in_cart"
    },
    {  # 5
        "name": "Добавити товар до кошика",
        "action": "add_to_cart"
    },
    {  # 6
        "name": "Видалити товар з кошика",
        "action": "remove_from_cart"
    },
    {  # 7
        "name": "Увійти як адміністратор",
        "action": "enter_admin_panel"
    },
    {  # 8
        "name": "Вийти з програми",
        "action": "exit_program"
    },
]
ADMINS = {  # Логін: пароль
    "Admin1": "Admin1",
    "Admin2": "Admin2"
}

# Змінні
catalog = [
    {
        "name": "Кабель Type-C",
        "price": float(150),
        "in_stock": int(18)
    },
    {
        "name": "Повербанк 10000mAh",
        "price": float(799.99),
        "in_stock": int(10)
    },
    {
        "name": "Навушники дротові",
        "price": float(350.50),
        "in_stock": int(12)
    },
    {
        "name": "Бездротова мишка",
        "price": float(420),
        "in_stock": int(8)
    },
    {
        "name": "Флешка 64GB",
        "price": float(299),
        "in_stock": int(6)
    },
    {
        "name": "Чохол для телефона",
        "price": float(190.10),
        "in_stock": int(22)
    }
]

shopping_cart = []

available_commands = []

is_authenticated = False


# Внутрішні функції
def is_cart_empty():
    if not shopping_cart:
        print("Кошик порожній.")
        show_available_commands()
        return True
    return False


get_in_total = lambda: sum(item['price'] for item in shopping_cart)


# Функції консольних команд
def show_available_commands(commands_to_show=None):
    global available_commands  # Отримання доступу до глобальної змінної
    if commands_to_show is None:
        commands_to_show = range(1, len(COMMANDS) + 1)

    available_commands.clear()  # Очищення списку доступних команд
    for command_num in commands_to_show:
        available_commands.append(COMMANDS[command_num - 1])

    print("")
    print("Список команд:")

    for command_num, command in enumerate(available_commands):
        print(f"{command_num + 1}. {command['name']}")


def show_catalog():
    print("Каталог товарів:")
    for item_num, item in enumerate(catalog):
        print(f"{item_num + 1}. {item['name']} - {item['price']:.2f} грн")

    show_available_commands([1, 3, 5, 8])


def show_cart():
    if is_cart_empty():
        return

    print("Кошик:")
    for item_num, item in enumerate(shopping_cart):
        print(f"{item_num + 1}. {item['name']} - {item['price']:.2f} грн")

    print(f"Загальна сума: {get_in_total():.2f} грн")

    show_available_commands([1, 4, 6, 8])


def buy_products_in_cart():
    if is_cart_empty():
        return

    print(f"Куплено товари в кошику на суму: {get_in_total():.2f} грн")
    shopping_cart.clear()
    show_cart()


def add_to_cart():
    choice = input("Введіть номер товару, який хочете додати до кошика: ")
    if not choice.isdigit():
        print("Невірний формат вводу.")
        return

    choice = int(choice) - 1
    if choice < 0 or choice >= len(catalog):
        print("Товар не знайдено.")
        return

    product_to_add = catalog[choice].copy()
    shopping_cart.append(product_to_add)

    print(f'Товар "{product_to_add["name"]}" додано до кошика.')
    print("")
    show_cart()


def remove_from_cart():
    if is_cart_empty():
        return

    choice = input("Введіть номер товару в кошику, який хочете видалити: ")

    if not choice.isdigit():
        print("Невірний формат вводу.")
        return

    choice = int(choice) - 1
    if choice < 0 or choice >= len(shopping_cart):
        print("Товар не знайдено у кошику.")
        return

    removed_item = shopping_cart.pop(choice)
    print(f'Товар "{removed_item['name']}" видалено з кошика.')
    print("")
    show_cart()


def enter_admin_panel():
    global is_authenticated

    if not is_authenticated:
        login = str(input("Введіть логін: "))
        password = str(input("Введіть пароль: "))

        if ADMINS.get(login) == password:
            is_authenticated = True
            print("Авторизація успішна.")
        else:
            print("Невірний логін або пароль.")
            return

    print("Залишок товарів:")
    for item_num, item in enumerate(catalog):
        print(f"{item_num + 1}. {item['name']} - {item['in_stock']} одиниць")

    show_available_commands([1, 8])


# Постійне очікування вводу користувача
def wait_for_input():
    while True:
        print("")
        choice = input("Введіть номер команди: ")

        if not choice.isdigit():
            print("Невірний формат вводу.")
            continue

        choice = int(choice) - 1

        if 0 <= choice <= len(available_commands):
            if available_commands[choice]["action"] == "exit_program":
                break

            func_name = available_commands[choice]["action"]
            globals()[func_name]()
        else:
            print("Невірний номер команди.")


# Точка входу
if __name__ == "__main__":
    show_available_commands()
    wait_for_input()
