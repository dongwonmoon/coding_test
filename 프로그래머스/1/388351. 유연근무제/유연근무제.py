def solution(schedules, timelogs, startday):
    days = {i+1: d for i, d in enumerate("월화수목금토일")}
    day_timelog = dict()
    
    for employee, timelog in enumerate(timelogs):
        d_l = dict()
        for d, log in enumerate(timelog):
            day = days[(startday+d-1)%7+1]
            if day in ["토", "일"]:
                continue
            d_l[day] = log
        day_timelog[employee] = d_l
    
    count = 0
    for employee, schedule in enumerate(schedules):
        ALL = True
        agree = schedule + 10
        if agree % 100 >= 60:
            agree += 40
        for log in day_timelog[employee].values():
            if log > agree:
                ALL = False
                break
        if ALL:
            count += 1
            
    return count
          