class MyClass(object):
    mMyPub=1
    __mMyPri=1
    def __init__(self,x,y):
        self.mMyPub=x
        self.__mMyPri=y

    def funPub(self):
        print("fun1")

    def __funPri(self):
        print("fun2")


class MyClass2(object):
    mMyPub=1
    __mMyPri=1
    def __init__(self,x,y):
        self.mMyPub=x
        self.__mMyPri=y

    def funPub(self):
        print("fun1")

    def __funPri(self):
        print("fun2")

