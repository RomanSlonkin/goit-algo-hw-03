from datetime import datetime

def get_days_from_today(date):
    requsted_date = datetime.strptime(date, "%Y-%m-%d").date()
    date_today = datetime.today().date()
    days_from_today = date_today - requsted_date
    print(days_from_today.days)

get_days_from_today("2026-10-09") 
