#zavdanya 1
numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
positives = []
negatives = []
evens = []
multiples_of_3 = []
for num in numbers:
    if num > 0:
        positives.append(num)
    elif num < 0:
        negatives.append(num)
        
    if num % 2 == 0:
        evens.append(num)
        
    if num % 3 == 0:
        multiples_of_3.append(num)
min_val = min(numbers)
max_val = max(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"Додатні: {positives}")
print(f"Від’ємні: {negatives}")
print(f"Парні: {evens}")
print(f"Кратні 3: {multiples_of_3}")
print(f"Min: {min_val}; Max: {max_val}; Sum: {total_sum}; Average: {average}")

#zavdanya 2
group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

common = group1 & group2         
only_group1 = group1 - group2     
only_group2 = group2 - group1     
all_users = group1 | group2       

print(f"Спільні: {', '.join(sorted(common))}")
print(f"Тільки group1: {', '.join(sorted(only_group1))}")
print(f"Тільки group2: {', '.join(sorted(only_group2))}")
print(f"Усі: {', '.join(sorted(all_users))}")

#zavdanya 3
catalog = {
    'milk': 48,
    'bread': 25,
    'tea': 75,
    'coffee': 120,
    'water': 15
}

catalog['chocolate'] = 65  
catalog['milk'] = 50       

search_name = 'tea'
price = catalog.get(search_name)
if price is not None:
    print(f"Знайдено товар: {search_name} — {price} грн")
else:
    print(f"Товар '{search_name}' не знайдено в каталозі.")

print("-" * 30)

min_price = 40
max_price = 100

print(f"Ціновий діапазон: {min_price}..{max_price} грн")
for name, price in catalog.items():
    if min_price <= price <= max_price:
        print(f"{name} — {price} грн")

#zavdanya 4
group_info = ('10-IT', '2026/2027')

journal = {
    'Anna': [10, 12, 8, 11, 9],
    'Ivan': [8, 9, 10, 11, 9]
}

def add_student(journal_dict, name, grades):
    if len(grades) != 5:
        print(f"Помилка: учень {name} повинен мати рівно 5 оцінок!")
        return False
    for grade in grades:
        if not (1 <= grade <= 12):
            print(f"Помилка: оцінка {grade} виходить за межі діапазону 1-12!")
            return False
    
    journal_dict[name] = grades
    return True

add_student(journal, 'Oleg', [11, 12, 10, 12, 11])

print(f"{group_info[0]} — {group_info[1]}\n")

print("--- Журнал та середній бал ---")
student_averages = {} 

for student, grades in journal.items():
    avg = sum(grades) / len(grades)
    student_averages[student] = avg
    print(f"{student} — {avg:.1f}")

print("\n--- Рейтинг учнів (від найвищого до найнижчого) ---")
sorted_rating = sorted(student_averages.items(), key=lambda item: item[1], reverse=True)

for rank, (student, avg) in enumerate(sorted_rating, start=1):
    print(f"{rank}. {student}: {avg:.1f}")

best_student, best_avg = max(student_averages.items(), key=lambda item: item[1])

print(f"\nНайкращий результат: {best_student} — {best_avg}")