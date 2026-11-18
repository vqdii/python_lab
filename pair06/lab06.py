import math
import random
import statistics
import datetime


def task1():
    print("=== Завдання 1. Геометричні обчислення ===")
    try:
        radius = float(input("Радіус: "))
        a = float(input("Катет 1: "))
        b = float(input("Катет 2: "))
        items = int(input("Предметів: "))
        per_box = int(input("В упаковці: "))
        if radius < 0 or a <= 0 or b <= 0 or items < 0 or per_box <= 0:
            print("Помилка: значення мають бути додатними.")
            return
    except ValueError:
        print("Помилка: введіть числа.")
        return

    area = math.pi * radius ** 2
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    boxes = math.ceil(items / per_box)

    print(f"Площа круга: {round(area, 2)}")
    print(f"Гіпотенуза: {round(hypotenuse, 2)}")
    print(f"Потрібно упаковок: {boxes}")


def task2():
    print("=== Завдання 2. Генератор оцінок ===")
    value = input("N (кількість оцінок): ")
    if not value.isdecimal() or int(value) <= 0:
        print("Помилка: N має бути додатним цілим числом.")
        return
    n = int(value)

    grades = [random.randint(1, 12) for _ in range(n)]
    high = len([g for g in grades if 10 <= g <= 12])

    print(f"Оцінки: {grades}")
    print(f"Min: {min(grades)}")
    print(f"Max: {max(grades)}")
    print(f"Середнє: {round(statistics.mean(grades), 2)}")
    print(f"Медіана: {statistics.median(grades)}")
    print(f"Оцінок 10–12: {high}")


def task3():
    print("=== Завдання 3. Дата події ===")
    try:
        year = int(input("Рік: "))
        month = int(input("Місяць: "))
        day = int(input("День: "))
        event = datetime.date(year, month, day)
    except ValueError:
        print("Помилка: некоректна дата.")
        return

    today = datetime.date.today()
    delta = (event - today).days

    if delta > 0:
        print(f"До події залишилося: {delta} днів")
    elif delta < 0:
        print(f"З моменту події минуло: {abs(delta)} днів")
    else:
        print("Подія відбувається сьогодні!")


if __name__ == "__main__":
    task1()
    print()
    task2()
    print()
    task3()
