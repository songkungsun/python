class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("Hello, my name is " + self.name)
        print("I'm %d years old." % self.age)


p1 = Person('song', 26)
p1.myfun()