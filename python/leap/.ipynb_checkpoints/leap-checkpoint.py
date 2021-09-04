# import calendar
# def leap_year(year):
#     return calendar.isleap(year)


# A leap in four years, no leap in one hundred years, four hundred years leap again.
def leap_year(year):    
    return True if (year % 100!=year % 4 == 0 or year%4 ==year%400==0) else False