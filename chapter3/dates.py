#
# Practicing Dates
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Date Objects
    # Get today's date
    today = date.today()
    print("Todays date is : ", today)

    # print day month year individually
    print("Date Components : ", today.day, today.month, today.year)

    print("Todays weekday number : ", today.weekday())

    today = datetime.now()
    print(today)

    t = datetime.time(datetime.now())
    print(t)

if __name__ == '__main__':
    main()
