#-------------------------------------- Function ----------------------------------------------


#============ Function Argument Types 



#----- default argument


# def greet(name="User"):
#     print(f"Hello, {name}")
# greet()
# greet("sinan")



#------ Keyword Argument


# def greet(name, age):
#     print(f"{name} is {age} years old")
# greet(name="Sinan",age=19)



#----- Positional Argument


# def greet(name, age):
#     print(f"{name} is {age} years old")
# greet("sinan", 19)



#----- Variable-Length Argument


# def add(*args):
#     return sum(args)
# print(add(1,2,3,4,5))



# def student(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} = {v}")
# student(name="Sinan", age= 19, place= "Kottakkal")






#============= Function Types Based on Argument & return value


#--------Without Argument & Without Return value


# def greet():
#     print("Hello")
# greet()




#------- With Argument but Without Return value


# def greet(name):
#     print("Hello", name)
# greet("Sinan")




# Without Argument but With return value


# def PI_value():
#     return 2.300
# print(PI_value())
    



# With Argument & With Return Value


# def greet(name,age):
#     print(f"{name} is {age} years old")
# greet("sinan",19)