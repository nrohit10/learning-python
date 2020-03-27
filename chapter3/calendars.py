#
# Practicing Calendars
#

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2020, 3, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2020, 3)
print(st)

for name in calendar.month_name:
    print(name)

print("Team meeting will be on")
for m in range(1, 13):
    cal = calendar.monthcalendar(2020, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
