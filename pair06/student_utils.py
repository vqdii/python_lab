import random


def generate_grades(count):
    """Повертає список із count випадкових оцінок від 1 до 12."""
    return [random.randint(1, 12) for _ in range(count)]


def average_grade(grades):
    """Повертає середній бал (0, якщо список порожній)."""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_level(average):
    """Повертає рівень успішності за середнім балом."""
    if average >= 10:
        return "високий"
    if average >= 7:
        return "достатній"
    if average >= 4:
        return "середній"
    return "початковий"
