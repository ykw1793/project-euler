from . import usage

def solution():
    # PyPy ~ 40 µs

    def is_leap_year(y):
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    return True
                return False
            return True
        return False
    
    # Jan = 0 ... Dec = 11
    month_days = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

    day = 1 # Sun = 0 ... Sat = 6 # 1 Jan 1900 = Monday
    year = 1900
    day = (day+366) % 7 if is_leap_year(year) else (day+365) % 7
    year += 1 # 1 Jan 1901
    month = 0
    
    num_sundays = 0
    while year < 2001:
        if day == 0:
            num_sundays += 1
        day = (day + month_days[month]) % 7 # Add a month
        if month == 1 and is_leap_year(year):
            day = (day+1) % 7 # Add one more day for leap year
        if month == 11:
            month = 0
            year += 1
        else:
            month += 1
    return num_sundays


if __name__ == '__main__':
    usage.usage(solution)