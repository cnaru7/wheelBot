from random import randrange


# wheel class
class myWheel:
    # array containing choices of the wheel

    # constructor of myWheel.
    def __init__(self, name, wheel):
        self.__wheelName = name  # set wheel name to given name.
        if len(wheel) >= 1:
            self.__wheel = wheel  # add elements from arguments to wheel.
        else:
            self.__wheel = []  # empty list

    # add a single choice to the wheel.
    def add(self, choice):
        self.__wheel.append(choice)

    # remove a single choice to the wheel.
    def remove(self, choice):
        try:
            self.__wheel.remove(choice)
        except ValueError:
            return False
        return True

    # spin the wheel.
    def spin(self):
        return self.__wheel[randrange(0, len(self.__wheel))]

    # set the name of the wheel.
    def setName(self, name):
        self.__wheelName = name

    # get the name of the wheel.
    def getName(self):
        return self.__wheelName

    # check if wheel is empty.
    def isEmpty(self):
        return len(self.__wheel) == 0

    # return wheel as an array.
    def getWheel(self):
        return self.__wheel
