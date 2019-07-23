import calendar

year = int(input("enter the year: "))
month = 1
print("\n********Calendar*********")
print()
# An instance of TextCalendar class is created and calendar.SUNDAY means that we need to start displaying the calendar froom Sunday
cal = calendar.TextCalendar(calendar.SUNDAY)

while month<=12:
    cal.prmonth(year,month) # prmonth() prints the calendar for given month and year
    month+=1
