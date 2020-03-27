#
# Practice file for loops
#

def main():
    x = 0

    # define a while loop
    while x < 5:
        print(x)
        x += 1

    # define a for loop
    for x in range(5, 10):
        print(x)

    # use a for loop over a collection
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for d in days:
        print(d)

    # use the break and continue statements
    for x in range(5, 10):
        if x == 7:
            # break
            continue
        print(x)

    # use the enumerate() function to get index
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for d in days:
        print(d)

if __name__ == '__main__':
    main()
