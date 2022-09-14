class SuperClass:

    def __init__(self):
        print("I am Super")

    def super_method(self):
        print("I am Super Method")

class SuperClass2:
    def __init__(self):
        print("I am Super 2")

    def super_method(self):
        print("I am Super 2 Method")


class SubClass(SuperClass, SuperClass2):

    def __init__(self):
       # super(SubClass, self).__init__()
       super().__init__()
       SuperClass2.__init__(self)
       print("Child class is created")

    def subclass_method(self):
        super().super_method()
        SuperClass2.super_method(self)
        print("Sub Class Logic for subclass_method")

child = SubClass()
child.subclass_method()