"""
MRO-Method Resolution Order is the order in which python looks for method in a hierarchy
Single method is availavle in multiple classes
"""

class classA:
    def methodA(self):
        print("I am coming from class A")

    def hello_world(self):
        print("Hello from class A")


class classB():
    def methodB(self):
        print("I am coming from class B")

    def hello_world(self):
        print("Hello from class B")

class classC(classB,classA):
    def methodC(self):
        print("I am coming from class c")

c=classC()
c.methodC()
c.hello_world()
print(classC.mro())

