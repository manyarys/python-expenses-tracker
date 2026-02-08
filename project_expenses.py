FILENAME = "expenses.txt"
total = 0

# Загружаем прошлые расходы
try:
    with open(FILENAME, "r") as file:
        for line in file:
            total += float(line.strip())
except FileNotFoundError:
    pass

print("Учёт расходов")
print("Вводи суммы расходов. 'q' — выход.\n")
print(f"Текущая сумма: {total}\n")

while True:
    value = input("Расход: ")

    if value == "q":
        break

    if not value.replace(".", "", 1).isdigit():
        print("Нужно ввести число.")
        continue

    expense = float(value)
    total += expense

    with open(FILENAME, "a") as file:
        file.write(f"{expense}\n")

    print(f"Добавлено: {expense}")
    print(f"Всего расходов: {total}\n")

print(f"Итоговая сумма расходов: {total}")
