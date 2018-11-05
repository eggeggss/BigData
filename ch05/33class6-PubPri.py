class MyClass(object):
    mMyPub=1
    __mMyPri=1
    def __init__(self,x,y):
        self.mMyPub=x
        self.__mMyPri=y
    @staticmethod
    def funPub():
        print("fun1")

    def __funPri(self):
        print("fun2")



g=MyClass(7,7)
#print(g.mMyPub)
#print(g.__mMyPri)
#g.funPub()
MyClass.mMyPub=200
print(MyClass.mMyPub)
print(MyClass.funPub())
#g.__funPri()






