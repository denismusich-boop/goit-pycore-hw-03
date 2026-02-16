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
