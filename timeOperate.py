import datetime
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

def getNextMonthDay(now,monthDay):
    if monthDay > now.day:
        return monthDay - now.day
    else:
        return monthDay - now.day + getMonthDays(now.month)
    pass
timeZero = datetime.timedelta(days=0)
time1Days = datetime.timedelta(days=1)
time7Days = datetime.timedelta(days=7)
time14Days = datetime.timedelta(days=14)
time30Days = datetime.timedelta(days=30)
time1seconds = datetime.timedelta(seconds=1)
time1Minutes = datetime.timedelta(minutes=1)
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

def weekdayStr2Weekday(s)->int:
    if s == "周一":
        return 0
    if s == "周二":
        return 1
    if s == "周三":
        return 2
    if s == "周四":
        return 3
    if s == "周五":
        return 4
    if s == "周六":
        return 5
    if s == "周日":
        return 6

if __name__ == '__main__':
    weekDay2Str()
