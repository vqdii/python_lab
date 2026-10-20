# завдання 1
text = input("Введіть довільний текст: ")

total_chars = len(text)
letters_count = 0
digits_count = 0
spaces_count = 0
glasni_count = 0

glasni = "aeiouyаеєиіїоуюя"

for char in text:
    if char.isalpha():
        letters_count += 1
        if char.lower() in glasni:
            glasni_count += 1
    elif char.isdigit():
        digits_count += 1
    elif char.isspace():
        spaces_count += 1

words_list = text.split()
words_count = len(words_list)

print(f"Символів: {total_chars}")
print(f"Літер: {letters_count}")
print(f"Цифр: {digits_count}")
print(f"Пробілів: {spaces_count}")
print(f"Голосних: {glasni_count}")
print(f"Слів: {words_count}")

# завдання 2
full_name = input("Введіть ПІБ одним рядком (Прізвище Ім'я По батькові): ")

parts = full_name.split()

if len(parts) == 3:
    last_name = parts[0].capitalize()
    first_name = parts[1].capitalize()
    second_name = parts[2].capitalize()
    
    first_initial = first_name[0]
    second_initial = second_name[0]
    
    # Склеюємо результат
    result_name = f"{last_name} {first_initial}.{second_initial}."
    print("Результат завдання 2:", result_name)
else:
    print("Помилка: Ви ввели не 3 частини ПІБ!")


# завдання 3
line1 = input("Введіть перший рядок: ")
line2 = input("Введіть другий рядок: ")

clean_line1 = ""
for char in line1:
    if char != " ":
        clean_line1 += char.lower()

clean_line2 = ""
for char in line2:
    if char != " ":
        clean_line2 += char.lower()

sorted_line1 = sorted(clean_line1)
sorted_line2 = sorted(clean_line2)

print("\nРезультат завдання 3:")
if sorted_line1 == sorted_line2:
    print(f"Рядки '{clean_line1}' та '{clean_line2}' є анаграмами.")
else:
    print(f"Рядки '{clean_line1}' та '{clean_line2}' не є анаграмами.")


# завдання 4
sentence = input("Введіть речення: ")

words = sentence.split()

longest_words = []
shortest_words = []
unique_words = []

if len(words) > 0:
    max_len = len(words[0])
    min_len = len(words[0])
    
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
        if len(word) < min_len:
            min_len = len(word)
            
    for word in words:
        if len(word) == max_len and word not in longest_words:
            longest_words.append(word)
        if len(word) == min_len and word not in shortest_words:
            shortest_words.append(word)
        
        if word.lower() not in unique_words:
            unique_words.append(word.lower())

print("\nРезультат завдання 4:")
print("Найдовші:", ", ".join(longest_words))
print("Найкоротші:", ", ".join(shortest_words))
print("Унікальних слів:", len(unique_words))

word_to_replace = input("\nВведіть слово для заміни: ")
new_word = input("Введіть нове слово: ")

updated_sentence = sentence.replace(word_to_replace, new_word)
print("Після заміни:", updated_sentence)