#======================= Polymorphism ==========================================



#------- Method OverLoading


# class Math:
#     def add(self, a=0, b=0, c=0):
#         return a + b + c

# m = Math()
# print(m.add(2,4))
# print(m.add(2,4,6))
# print(m.add())




#-------- Operator Overloading


# class Book:
#     def __init__(self, pages):
#         self.pages = pages
    
#     def __add__(self, other):
#         return self.pages + other.pages
    
# book1 = Book(150)
# book2 = Book(250)
    
# print(book1 + book2)






#-------- Method Overriding


# class Animal:
#     def sound(self):
#         print("Animal Sounds")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")
    
# animals = [Dog(), Cat(), Animal()]
# for a in animals:
#     a.sound()





#------- Built-in (Duck Typing)


# class Dog:
#     def sound(self):
#         return "Bark"

# class Cat:
#     def sound(self):
#         return "Moew"

# def make_sound(animal):
#     print(animal.sound())

# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)