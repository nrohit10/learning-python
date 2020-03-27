def main():
    # f = open("textfile.txt", "w+")
    # f = open("textfile.txt", "a")
    f = open("textfile.txt", "r")

    # for i in range(11, 21):
    #     f.write("This is line : " + str(i) + "\r\n")

    if f.mode == 'r':
        contents = f.read()
        print(contents)

    f.close()

if __name__ == '__main__':
    main()