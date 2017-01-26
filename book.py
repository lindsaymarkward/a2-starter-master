# create your simple Book class in this file
class Book:
    __title = ""
    __author = ""
    __page = 0
    __status = 'r'

    def __init__(self, t, a, p, s):
        self.__title = t
        self.__author = a
        self.__page = p
        self.__status = s

    def __str__(self):
        printStr = self.__title + " by " + self.__author + ", " + self.__page + " pages ("

        if self.__status == 'r':
            printStr += 'Required'
        else:
            printStr += 'Completed'
        printStr += ')'
        return printStr

    def getTitle(self):
        return self.__title

    def getStatus(self):
        return self.__status

    def getPage(self):
        return self.__page

    def markComplete(self):
        self.__status = 'c'

    def isLong(self):
        if self.__page > 500:
            return True
        else:
            return False

    def isBefore(self, compare):
        if compare.__author < self.__author:
            return False
        elif self.__author == compare.__author and self.__page > compare.__page:
            return False
        else:
            return True