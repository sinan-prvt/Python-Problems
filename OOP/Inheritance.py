#=============================== Inheritance ====================================================


# class Animal():
#     def speak(self):
#         print("Animal Speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")

# dog = Dog()
# dog.speak()






#------ Single Inheritance


# class Parent:
#     def greet(self):
#         print("Hello, From Parent")
    
# class Child(Parent):
#     def play(self):
#         print("Child is Playing")

# c = Child()

# c.greet()
# c.play()





#----- Multiple Inheritance


# class Parent:
#     def skill(self):
#         print("Diving")

# class Mother:
#     def hobby(self):
#         print("Cooking")

# class Child(Parent, Mother):
#     pass

# c = Child()
# c.skill()
# c.hobby()






#-------- Multilevel Inheritance


# class Grandparent:
#     def home(self):
#         print("Grand Parent House")
    
# class Parent(Grandparent):
#     def car(self):
#         print("Parent Car")

# class Child(Parent):
#     def bike(self):
#         print("Child Bike")

# c = Child()
# c.home()
# c.car()
# c.bike()







#------ Hierarchical Inheritance


# class Parent:
#     def work(self):
#         print("Parent Work Hard")

# class Son(Parent):
#     def hobby(self):
#         print("Son Likes Football")

# class Daughter(Parent):
#     def hobby(self):
#         print("Daugter Likes Painting")

# s = Son()
# d = Daughter()

# s.work() ; s.hobby()
# d.work() ; d.hobby()








#------ Hybrid Inheritance


# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         print("Class B")

# class C(A):
#     def show(self):
#         print("Class C")
    
# class D(B, C):
#     pass

# d = D()
# d.show()