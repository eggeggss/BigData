import random
from abc import ABCMeta, abstractmethod


class Flyer(metaclass=ABCMeta):  # 就像是Java中的interface
    @abstractmethod
    def fly(self):
        pass

class Dog:
    pass
    def bark(self):
        print('旺旺')

class Bird:
    pass
    def bark(self):
        print('咪咪')

class Sparrow(Bird, Dog):  # 就像Java中繼承Bird類別並實作Flyer介面
    def fly(self):
        print('麻雀飛')

    def bark(self):
        super().bark()

s = Sparrow()
s.fly()
s.bark()