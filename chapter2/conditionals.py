#
# Practice file for conditionals
#

def main():
    x, y = 100, 1000

    # conditional flow uses if, elif, else
    if x < y:
        st = "x is less than y"
    elif x == y:
        st = "x is same as y"
    else:
        st = "x is greater than y"

    print(st)

    # conditional statement let you use "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater than y or x is same as y"
    print(st)


if __name__ == "__main__":
    main()