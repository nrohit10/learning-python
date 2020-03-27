#
# Praticing date time formatting
#

from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("The current year is : %Y"))
    print(now.strftime("%a, %d, %B, %y"))

    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date and time: %x"))
    print(now.strftime("Locale date and time: %X"))

    print(now.strftime("Current Time: %I:%M:%S %p"))
    print(now.strftime("Current Time: %H:%M"))

if __name__ == '__main__':
    main()