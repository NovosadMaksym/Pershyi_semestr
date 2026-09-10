print("Hello World")

print(50 * "-")

integer = 3
floatVariable = 3.14
string = "text"
boolean = True
listVariable = [1, 2, 3]
tupleVariable = (1, 2, 3)
dictionary = {1: "one", 2: "two", 3: "three"}
setVariable = {1, 2, 3, 3}

print(integer, type(integer))
print(floatVariable, type(floatVariable))
print(string, type(string))
print(boolean, type(boolean))
print(listVariable, type(listVariable))
print(tupleVariable, type(tupleVariable))
print(dictionary, type(dictionary))
print(setVariable, type(setVariable))

print(20 * "-")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

print(a ,"+", b, "=", a+b) # Додавання
print(a, "-", b, "=", a-b) # Віднімання
print(a, "/", b, "=", a/b) # Ділення
print(a, "*", b, "=", a*b) # Множення
print(a, "%", b, "=", a%b) # Остача від ділення
print(a, "//", b, "=", a//b) # Цілочисленне ділення
print(a, "**", b, "=", a**b) # Зведення в степінь

print(20*"-")

if a > b:
    print(a, ' є більшим за ', b)
elif a < b:
    print(a, ' є меншим за ', b)
else:
    print(a, ' дорівнює ', b)