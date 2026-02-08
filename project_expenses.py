FILENAME = "expenses_v3.txt"

totals_by_category = {}

def load_data():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",", 1)
                if len(parts) != 2:
                    continue

                category = parts[0].strip().lower()
                amount = float(parts[1].strip())

                totals_by_category[category] = totals_by_category.get(category, 0) + amount
    except FileNotFoundError:
        pass

def print_report():
    print("\nОтчёт по категориям:")
    if not totals_by_category:
        print("Пока нет расходов.")
        return

    grand_total = 0
    for category, amount in sorted(totals_by_category.items()):
        print(f"- {category}: {amount:.2f}")
        grand_total += amount

    print(f"\nИТОГО: {grand_total:.2f}\n")

def is_number(value: str) -> bool:
    value = value.strip()
    if value.count(".") > 1:
        return False
    return value.replace(".", "", 1).isdigit()

load_data()

print("Учёт расходов v3 (категории)")
print("Формат ввода: категория сумма")
print("Пример: food 12.50")
print("Команды: report | q\n")

print_report()

while True:
    text = input("Ввод: ").strip()

    if text.lower() == "q":
        break

    if text.lower() == "report":
        print_report()
        continue

    parts = text.split()
    if len(parts) != 2:
        print("Нужно: категория сумма (например: food 12.50)")
        continue

    category = parts[0].strip().lower()
    amount_str = parts[1].strip()

    if not is_number(amount_str):
        print("Сумма должна быть числом.")
        continue

    amount = float(amount_str)

    # сохраняем в файл
    with open(FILENAME, "a") as file:
        file.write(f"{category},{amount}\n")

    # обновляем суммы в памяти
    totals_by_category[category] = totals_by_category.get(category, 0) + amount

    print(f"Добавлено: {category} {amount:.2f}")

print_report()
print("Пока!")
