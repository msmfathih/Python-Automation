"""
MULTI LEVEL INHERITANCE
if same methods available classA classB and whn cl hello world
the method from classB will be called know as method overriding
"""
class classA:
    def methodA(self):
        print("I am coming from class A")

    def hello_world(self):
        print("Hello from class A")


class classB(classA):
    def methodB(self):
        print("I am coming from class B")

    def hello_world(self):
        print("Hello from class B")

class classC(classB):
    def methodC(self):
        print("I am coming from class c")




obj1=classC()
obj1.methodA()
obj1.methodB()
obj1.methodC()
obj1.hello_world()



