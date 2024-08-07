"""
Write a program that returns True or False whether if a given year is a leap year.
"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
    else:
        return False
