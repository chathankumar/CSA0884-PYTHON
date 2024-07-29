import datetime
def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")
day = 31
month = 8
year = 2019
print(get_day_of_week(day, month, year))
