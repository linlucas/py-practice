class SomeClass:
    def __init__(self):
        print('super class constructor invoked')
        SomeClass.saying = 'superclass'


class ChildClass(SomeClass):
    def __init__(self):
        super().__init__()
        self.cool = True

    def get_something(self):
        print('this is a method')


child = ChildClass()
