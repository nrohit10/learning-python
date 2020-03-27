#
# Practicing os path util
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    print("Item Exists : " + str(path.exists("textfile.txt")))
    print("Item is a file : " + str(path.isfile("textfile.txt")))
    print("Item is a directory : " + str(path.isdir("textfile.txt")))
    print("Item Path : " + str(path.realpath("textfile.txt")))
    print("Item Path and name : " + str(path.split(path.realpath("textfile.txt"))))

    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since it was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == '__main__':
    main()