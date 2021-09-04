import calendar
from datetime import date


def meetup(year, month, week, day_of_week):
    week_dic=dict(zip(calendar.day_name,range(7)))
    cal=calendar.Calendar()
    # i ,index 0 is day ,index 1 is weekday
    days=[i[0] for i in cal.itermonthdays2(year,month) if i[0]!=0 and i[1]==week_dic.get(day_of_week)]

    if week=='last':
        day=days[-1]
    elif week=='teenth':
        day=filter(lambda x:13<=x<=19,days).__next__()
    else:
        if int(week[0])>len(days):
            raise MeetupDayException(f"week is error, There's no {week} {day_of_week} this month")
        week_num=int(week[0]) 
        day=days[int(week_num-1)]
    return date(year,month,day)


class MeetupDayException(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo


    def __str__(self):
        return self.errorInfo

