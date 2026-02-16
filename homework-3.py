from datetime import datetime
def get_days_from_today(date):
    given_date = datetime.strptime(date,"%Y-%m-%d").date()
    today = datetime.now().date()
    diff = (today - given_date).days
    return diff

print("days of war:", get_days_from_today("2022-02-24"))


import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 999, 10)
print("Ваші лотерейні числа:", lottery_numbers)


print("Завдання 3")

import re

def normalize_phone(phone_number):
    norm = re.sub(r"[^\d+]", "", phone_number)

    if norm.startswith("+"):
        return norm
    if norm.startswith("380"):
        return "+" + norm
    return "+38" + norm

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
print(normalize_phone("38050-123-4567"))
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

Print("Завдання 4")

from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = bday.replace(year=today.year)

        # якщо вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # перевіряємо, чи входить у вікно [сьогодні; сьогодні+7]
        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # перенос з вихідних на понеділок
            weekday = congratulation_date.weekday()  # Mon=0 ... Sun=6
            if weekday == 5:       # Saturday
                congratulation_date += timedelta(days=2)
            elif weekday == 6:     # Sunday
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Wova", "birthday": "1990.02.21" },
    {"name": "Ben Down", "birthday": "1999.02.18"},
]
print (get_upcoming_birthdays (users))


