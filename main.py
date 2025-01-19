class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def  make_sound(self):
        print("Meow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        print("Bark")
cat1 = Cat("Crookshanks",10)
Dog1 = Dog("Timmy",9.5)
for animal in(cat1,Dog1):
    animal.make_sound()
    print(f"Hello i am cat.My name is {animal.name}.My age is{animal.age}")

#2activity
class Price:
    def __init__(self):
        self.__maxprice= 900
    def self(self):
         print(f"The max price is {self.__maxprice}")
    def setMaxprice(self,Price):
        self.__maxprice=Price

c=Price()
c.self()
c.__maxprice=1000
c.self()
c.setMaxprice(1000)
c.self()