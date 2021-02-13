class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    dogInfo = "All dogs of this class are cool!"
    def bark(self):
        print("bark")

mydog=Dog("Uno",13)
mydog.bark()

#mydog.name = "Uno"
print(mydog.name)
print(mydog.age)
print(mydog.dogInfo)


class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2020 - self.year

myClio = Car (2006,"Renault","Clio")
print(myClio.age())