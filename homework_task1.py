"""Module providing a function to work with date"""
from datetime import datetime

def get_days_from_today(date: datetime):
    """function to count difference in date and todays date in days  """
    try:
        requsted_date = datetime.strptime(date, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        days_from_today = requsted_date - date_today
        return days_from_today.days
    except ValueError:
        print("date does not match format YYYY-MM-DD'")
        

print(get_days_from_today("2024-25-09")) #test
# End-of-file (EOF)