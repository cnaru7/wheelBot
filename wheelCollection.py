from typing import List, Any
from wheel import myWheel


class wheelCollection:

    # constructor of myWheel
    def __init__(self):
        print("wheel collection created!")
        self.__wheelCollection: List[myWheel] = []  # initialize variable

    def inLibrary(self, name: str):
        j = 0
        for i in self.__wheelCollection:
            if i.getName() == name:
                return j
            j = j + 1
        return -1

    def addWheel(self, wheel: myWheel):
        if self.inLibrary(wheel.getName()) == -1:
            self.__wheelCollection.append(wheel)
            return False
        return True

    def removeWheel(self, wheelName):
        location = self.inLibrary(wheelName)
        if location > -1:
            self.__wheelCollection.pop(location)
            return False
        return True

    def addElements(self, wheelName, elements):
        location = self.inLibrary(wheelName)
        if location > -1:
            for i in elements:
                self.__wheelCollection[location].add(i)
            return False
        return True

    def removeElements(self, wheelName, elements):
        location = self.inLibrary(wheelName)
        if location > -1:
            for i in elements:
                if not self.__wheelCollection[location].remove(i):
                    return True
            return False
        return True

    def spinWheel(self, name: str):
        index = self.inLibrary(name)
        if index > -1:
            spin = self.__wheelCollection[index].spin()
            return spin
        return "Wheel does not exist!"

    def toString(self):
        for i in self.__wheelCollection:
            print(i.getName())


