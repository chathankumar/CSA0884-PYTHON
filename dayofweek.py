import datetime
def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date.weekday()
    return days_of_week[day_index]
day = 31
month = 8
year = 2019
print(get_day_of_week(day, month, year))
