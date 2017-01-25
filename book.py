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
        return ('{: <40}'.format(self.__title) + " by " + '{: <20}'.format(self.__author) + '{: >4}'.format(
            self.__page) + " pages")

    def markComplete(self):
        self.__status = 'c'

    def isLong(self):
        if self.__page > 500:
            return True
        else:
            return False