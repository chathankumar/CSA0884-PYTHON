def get_season(month, day):
    seasons = {
        'Winter': ('December', 21),
        'Spring': ('June', 21),
        'Summer': ('March', 20),
        'Fall': ('September', 22)
    }
    month = month.capitalize()
    season_boundaries = [
        ('Winter', 'Spring', 'December', 21, 'June', 21),
        ('Spring', 'Summer', 'June', 21, 'March', 20),
        ('Summer', 'Fall', 'March', 20, 'September', 22),
        ('Fall', 'Winter', 'September', 22, 'December', 21)
    ]
    month_days = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 
                   'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 
                   'November': 11, 'December': 12}
    
    input_month = month_days[month]
    input_day = day
    
    for season_start, next_season, start_month, start_day, end_month, end_day in season_boundaries:
        if (input_month > month_days[start_month] or
           (input_month == month_days[start_month] and input_day >= start_day)):
            if (input_month < month_days[end_month] or
               (input_month == month_days[end_month] and input_day < end_day)):
                return season_start

    return 'Invalid date'

def main():
    month = input("Enter the month: ")
    day = int(input("Enter the date: "))

    season = get_season(month, day)
    print(f"The season is currently {season}")

if __name__ == "__main__":
    main()
