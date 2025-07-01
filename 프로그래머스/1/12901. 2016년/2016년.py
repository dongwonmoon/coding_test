from datetime import date
import calendar

def solution(a, b):
    my_date = date(2016, a, b)
    return my_date.strftime("%A")[:3].upper()