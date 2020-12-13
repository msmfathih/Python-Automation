class person():
    def singing(self):
        print("I'm singing")

    def dancing(self):
        print("i'm dancing")

    def sum(self, num1, num2):
        print(num1+num2)



# p = pearson()
# p.dancing()
# p.singing()
# p.sum(10,20)


"""set property for person object"""
p = person()
p.name ="Fathih"
p.phone=52054545
p.country="Srilanka"

print(p.name)
print(p.country)