"""Module providing a function to work with date"""
from datetime import datetime

def get_days_from_today(date):
    """function to count difference in date and todays date in days  """
    requsted_date = datetime.strptime(date, "%Y-%m-%d").date()
    date_today = datetime.today().date()
    days_from_today = date_today - requsted_date
    print(days_from_today.days)

get_days_from_today("2021-05-09")
# End-of-file (EOF)