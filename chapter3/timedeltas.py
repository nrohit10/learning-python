#
# Practicing time deltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("Today is : ", str(now))

print("One year from now will be : ", str(now + timedelta(days=365)))

print("In 2 days and 3 weeks it will be : ", str(now + timedelta(days=2, weeks=3)))


today = date.today()
afd = date(today.year, 4, 1)

if(afd < today):
    print("April Fools Day already went by %d days ago" %((today-afd).days))
    afd = afd.replace(year=today.year+1)

time_to_afd = afd - today
print("Its just ", time_to_afd.days, "days until April Fools Day")