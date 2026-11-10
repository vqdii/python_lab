#завдання 1
import math

def circle_area(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def main():
    print("Оберіть фігуру (коло, прямокутник, трикутник):")
    shape = input("Фігура: ").strip().lower()
    
    if shape == "коло" or shape == "круг":
        radius = float(input("Радіус: "))
        area = circle_area(radius)
        print(f"Площа круга: {area}")
        
    elif shape == "прямокутник":
        width = float(input("Ширина: "))
        height = float(input("Висота: "))
        area = rectangle_area(width, height)
        if area.is_integer():
            area = int(area)
        print(f"Площа прямокутника: {area}")
        
    elif shape == "трикутник":
        base = float(input("Основа: "))
        height = float(input("Висота: "))
        area = triangle_area(base, height)
        if area.is_integer():
            area = int(area)
        print(f"Площа трикутника: {area}")
        
    else:
        print("Невідома фігура!")

if __name__ == "__main__":
    main()
    
#завдання 2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def main():
    n = int(input("N = "))
    
    prime_status = "так" if is_prime(n) else "ні"
    divs = divisors(n)
    d_sum = digit_sum(n)
    
    print(f"Просте число: {prime_status}")
    print(f"Дільники: {divs}")
    print(f"Сума цифр: {d_sum}")

if __name__ == "__main__":
    main()

#завдання 3
def average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def minimum(grades):
    if not grades:
        return 0
    return min(grades)

def maximum(grades):
    if not grades:
        return 0
    return max(grades)

def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count

def main():
    grades = [10, 8, 12, 9, 11]
    threshold = 9
    
    print(f"Оцінки: {grades}")
    print(f"Поріг: {threshold}\n")
    print("Результат")
    
    avg_score = average(grades)
    min_score = minimum(grades)
    max_score = maximum(grades)
    above_count = count_above(grades, threshold)
    
    print(f"Середній бал: {avg_score:.1f}")
    print(f"Мінімальна: {min_score}")
    print(f"Максимальна: {max_score}")
    print(f"Вище {threshold}: {above_count}")

if __name__ == "__main__":
    main()

#завдання 4
def check_length(password):
    return len(password) >= 8

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False

def validate_password(password):
    failed_requirements = []
    
    if not check_length(password):
        failed_requirements.append("мінімальна довжина менше 8 символів")
    if not has_digit(password):
        failed_requirements.append("немає жодної цифри")
    if not has_upper(password):
        failed_requirements.append("немає великої літери")
    if not has_lower(password):
        failed_requirements.append("немає малої літери")
    if not has_special(password):
        failed_requirements.append("немає спеціального символу")
        
    is_valid = len(failed_requirements) == 0
    return is_valid, failed_requirements

def main():
    password = input("Password: ")
    
    is_valid, errors = validate_password(password)
    
    if is_valid:
        print("Пароль надійний!")
    else:
        print("Пароль не відповідає вимогам.")
        for error in errors:
            print(f"Не виконано: {error}")

if __name__ == "__main__":
    main()