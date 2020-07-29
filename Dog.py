class Dog:
    """one attempt to simulate a little dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        print(self.name.title() + "rolled over!")


my_dog = Dog('WangCai', 1.5)

your_dog = Dog('Zaizai', 7)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old")
print("Your dog's name is " + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + " years old")
