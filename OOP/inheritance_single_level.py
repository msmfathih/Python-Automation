"""
Single level inheritance
"""
class Base:
    name = "fathih"
    def baseMethod(self):
        print("I'm in base class")

class Child(Base): 
    subject = "Automation"
    def childMethod(self):
        print("I'm in child class")

c=Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.subject)

