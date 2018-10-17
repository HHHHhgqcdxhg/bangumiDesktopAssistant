import datetime
import calendar
def getMonthDays(month):
    if month == 1:
        days = 31
    elif month == 2:
        days = 28
    elif month == 3:
        days = 31
    elif month == 4:
        days = 30
    elif month == 5:
        days = 31
    elif month == 6:
        days = 30
    elif month == 7:
        days = 31
    elif month == 8:
        days = 31
    elif month == 9:
        days = 30
    elif month == 10:
        days = 31
    elif month == 11:
        days = 30
    elif month == 1:
        days = 31
    return days
    return datetime.timedelta(days=days)

def getNextWeekDay(weekDay):
    if weekDay == 0:
        m1 = calendar.MONDAY
    elif weekDay == 1:
        m1 = calendar.TUESDAY
    elif weekDay == 2:
        m1 = calendar.WEDNESDAY
    elif weekDay == 3:
        m1 = calendar.TUESDAY
    elif weekDay == 4:
        m1 = calendar.FRIDAY
    elif weekDay == 5:
        m1 = calendar.SATURDAY
    elif weekDay == 6:
        m1 = calendar.SUNDAY
    return datetime.timedelta(days=m1 + 1 if m1 <= 5 else m1 - 6)

def getNextMonthDay(now,monthDay):
    if monthDay > now.day:
        return monthDay - now.day
    else:
        print(monthDay,now.day,getMonthDays(now.month))
        return monthDay - now.day + getMonthDays(now.month)
    pass
timeZero = datetime.timedelta(days=0)
time1Days = datetime.timedelta(days=1)
time7Days = datetime.timedelta(days=7)
time14Days = datetime.timedelta(days=14)
time30Days = datetime.timedelta(days=30)

def weekDay2Str(weekday):
    if weekday == 0:
        return "周一"
    if weekday == 1:
        return "周二"
    if weekday == 2:
        return "周三"
    if weekday == 3:
        return "周四"
    if weekday == 4:
        return "周五"
    if weekday == 5:
        return "周六"
    if weekday == 6:
        return "周日"


if __name__ == '__main__':
    weekDay2Str()
