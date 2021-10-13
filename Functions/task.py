import calendar

# number of days per month, first value placeholder for proper indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 31, 31, 31, 30, 31, 30, 31]


def month_and_day(year, month):
    """Returns the  number of day in the given month for the given year"""
    if month == 2 and calendar.isleap(year):
        return 29

    return month_days[month]


def get_input_month():
    """Gets input from user and returns as month value"""

    def month_error():
        print('Invalid month!')
        get_input_month()

    month = input('Enter a month: ')

    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            return month
        else:
            month_error()
    else:
        month_error()


def get_input_year():
    """Gets input from user and returns as year value"""
    year = input('Enter the year: ')

    if year.isdigit():
        year = int(year)
        return year
    else:
        print('Invalid input!')
        get_input_year()


check_month = get_input_month()
check_year = get_input_year()

print(month_and_day(check_year, check_month))
