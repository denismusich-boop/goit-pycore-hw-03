from datetime import datetime
def get_days_from_today(date):
    given_date = datetime.strptime(date,"%Y-%m-%d").date()
    today = datetime.now().date()
    diff = (today - given_date).days
    return diff

print("days of war:", get_days_from_today("2022-02-24"))
