users = {
    "Yevhen_Melnyk": {
        "password": "Melnyk2009",
        "marks": (10, 11, 8, 7, 12, 6, 2, 4, 3, 4),
    },
    "Anastasiia_Shevchenko": {
        "password": "Shevchenko2009",
        "marks": (8, 10, 5, 11, 7, 3, 8, 9, 12, 4),
    },
    "Oleksandr_Kovalenko": {
        "password": "Kovalenko2010",
        "marks": (12, 8, 10, 6, 5, 9, 4 , 4, 3, 11),
    },
    "Vladyslav_Bondarenko": {
        "password": "Bondarenko2009",
        "marks": (10, 9, 4, 3, 8, 12, 4, 7, 2, 8),
    },
}

login = str(input("Введіть логін: "))
password = str(input("Введіть пароль: "))

if login in users and password == users[login]["password"]:
    goodMarks = 0
    badMarks = 0

    for mark in users[login]["marks"]:
        if 12 >= mark >= 5:
            goodMarks += 1
        elif 1 <= mark <= 4:
            badMarks += 1

    print("Перелік оцінок: ", users[login]["marks"])
    print("Кількість задовільних оцінок: ", str(goodMarks))
    print("Кількість незадовільних оцінок: ", str(badMarks))
else:
    print("Невірний логін або пароль")
