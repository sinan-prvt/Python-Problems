#====================== Encapsulation ====================================================


#------ Public Encapsulation


# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
    
# s = Student("Sinan", 19)
# print(s.name)
# print(s.age)




#------  Protected Encapsulation


# class Student:
#     def __init__(self, name, age):
#         self._age = age
    
#     def show(self):
#         print("Age : ", self._age)
    
# s = Student("Sinan", 19)
# s.show()
# print(s._age)




#----- Private Encapsulation



# class Student:
#     def __init__(self, name, mark):
#         self.__mark = mark
    
#     def get_mark(self):
#         return self.__mark
    
#     def set_mark(self, mark):
#         if 0 <= mark <= 100:
#             self.__mark = mark
#         else:
#             print("Invalid Mark")

# s = Student("Sinan", 94)
# print(s.get_mark())
# s.set_mark(102)
# s.set_mark(83)
# print(s.get_mark())