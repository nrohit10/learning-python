#
# Practice classes
#

class myClass():
    def method1(self):
        print("My Class Method")

    def method2(self, someString):
        print("My CLass Method2", someString)


class myClass1(myClass):
    def method1(self):
        print("My Class1 Method")

    def method2(self, someString):
        print("My CLass1 Method2", someString)


def main():
    c = myClass()
    c.method1()
    c.method2("This is a String.")

    c1 = myClass1()
    c1.method1()
    c1.method2("This is a String.")


if __name__ == '__main__':
    main()