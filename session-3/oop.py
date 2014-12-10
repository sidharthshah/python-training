class Animal:
    num = 0

    #Constructor
    def __init__(self):
        self.num = 10

    #Method 1
    def addone(self):
        self.num += 1

    #Method 2
    def print_num(self):
        print self.num

    #Method with args
    def add(self, x):
        self.num += x

    def hello(self):
        print "Meow!"

class Dog(Animal):
    legs = 4

    def hello(self):
        print "Bhaw BahW!"

    def legs(self):
        print self.legs


if __name__ == "__main__":
    a = Animal()
    a.hello()

    kamina = Dog()
    kamina.hello()