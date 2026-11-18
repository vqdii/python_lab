import tkinter as tk
from tkinter import messagebox

import student_utils

STUDENTS = ["Anna", "Ivan", "Olha"]


def build_report(count):
    lines = []
    for name in STUDENTS:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        lines.append(f"{name}: {grades} → {round(avg, 2)} → {level}")
    return "\n".join(lines)


def on_click():
    value = entry.get().strip()
    if not value.isdecimal():
        messagebox.showerror("Помилка", "Введіть ціле число від 1 до 20.")
        return
    count = int(value)
    if not 1 <= count <= 20:
        messagebox.showerror("Помилка", "Кількість оцінок має бути від 1 до 20.")
        return

    report = build_report(count)
    print(report)
    print()

    text.delete("1.0", tk.END)
    text.insert(tk.END, report)


root = tk.Tk()
root.title("Статистика учнів")

label = tk.Label(root, text="Кількість оцінок для кожного учня (1–20):")
label.pack(padx=10, pady=5)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

button = tk.Button(root, text="Сформувати звіт", command=on_click)
button.pack(padx=10, pady=5)

text = tk.Text(root, width=70, height=10)
text.pack(padx=10, pady=10)

root.mainloop()
