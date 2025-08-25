#============================================ Class =============================================



#------- basic

# class Car:
#     def __init__(self, brand, model):                               #  Constructor
#         self.brand = brand
#         self.model = model

#     def display(self):                                              #  Method
#         print(f"Car: {self.brand} {self.model}")                     

# c1 = Car("Tesla","Model S")                                         # Creating Object(Instance)
# c2 = Car("Toyota","Etios")

# c1.display()
# c2.display()





#------- Methods in Class

#------- Instance Method

# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
    
#     def Info(self):                                                             #  Instance method
#         print(f"Car: {self.brand} is runs at {self.speed} km/h")

# c1 = Car("BMW", 230)
# c2 = Car("Alto", 190)

# c1.Info()
# c2.Info()




#------ Class Method


# class Student:                              #  class Variable
#     school = "Pkmmhss"

#     def __init__(self, name):               
#         self.name = name

#     @classmethod                            #  class Method
#     def display(cls, new_school):
#         cls.school = new_school

# s1 = Student("Sinan")
# s2 = Student("Shamil")

# print(Student.school)
# Student.display("ABC School")

# print(s1.school)
# print(s2.school)




#----- Static Method


# class Math:
#     @staticmethod
#     def add(a,b):
#         return a + b
    
#     @staticmethod
#     def square(x):
#         return x * x
    
# print(Math.add(3,4))
# print(Math.square(2))





#------- abstract Method


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# dog = Dog()
# cat = Cat()

# print(dog.sound())
# print(cat.sound())