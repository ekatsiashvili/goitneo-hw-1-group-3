from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.now()

    # Визначаємо дату на початок наступного тижня
    next_week_start = current_date + timedelta(days=(7 - current_date.weekday()))

    # Визначаємо дату на кінець наступного тижня
    next_week_end = next_week_start + timedelta(days=7)

    # Проходження через кожного користувача та перевірка, чи потрапляє його день народження у наступний тиждень
    upcoming_birthdays = []
    for user in users:
        if next_week_start <= user["birthday"] < next_week_end:
            upcoming_birthdays.append(user)

    # Вивід списку користувачів з днями народження на наступному тижні
    if upcoming_birthdays:
        print("Користувачі, яких потрібно привітати на наступному тижні:")
        for user in upcoming_birthdays:
            print(f"{user['name']} - {user['birthday'].strftime('%d.%m.%Y')}")
    else:
        print("Немає користувачів з днями народження на наступному тижні.")

# Приклад використання:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)}
]

get_birthdays_per_week(users)