class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 5)

my_dog.bark() # prints "Buddy says woof!"
