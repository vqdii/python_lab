# завдання 1

n = int(input("N = "))
total = 0
count = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        count += 1

print("Кількість:", count)
print("Сума:", total)

if count > 0:
    print("Середнє:", round(total / count, 2))
else:
    print("Середнє: немає таких чисел")

# завдання 2
n = int(input("N = "))

count = 0
total = 0
max_digit = 0
min_digit = 9

if n == 0:
    count = 1
    min_digit = 0
else:
    while n > 0:
        digit = n % 10
        count += 1
        total += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        n //= 10

print("Кількість цифр:", count)
print("Сума цифр:", total)
print("Найбільша цифра:", max_digit)
print("Найменша цифра:", min_digit)


# завдання 3
n = int(input("N = "))

for i in range(1, n + 1):
    number = i
    valid = True

    while number > 0:
        digit = number % 10

        if digit != 0 and i % digit != 0:
            valid = False
            break

        number //= 10

    if valid:
        print(i, end=" ")

print()


# завдання 4
width = int(input("Ширина: "))
height = int(input("Висота: "))
border = input("Символ контуру: ")
inside = input("Символ всередині: ")

if width < 3 or height < 3:
    print("Помилка: ширина та висота мають бути не менше 3.")
elif len(border) != 1 or len(inside) != 1:
    print("Помилка: потрібно ввести по одному символу.")
else:
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                print(border, end="")
            else:
                print(inside, end="")
        print()