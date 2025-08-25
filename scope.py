#------ Variable Scope    

# def greet() :
#     name = "Sinan"                     # Local VAriable      
#     print("Hello", name)
# greet()
# print(name)                            # Error



# name = "Sinan"                           #  Global Variable
# def greet() :
#     print("Hello", name)
# greet()
# print(name)


# name = "Siananu"                          # Global Keyword
# def greet():
#     global name
#     name = "Sinan"
#     print("Hello", name)
# greet()




# def outer():                              # Non-Local Keyword
#     msg = "Hi"
#     def inner():
#         nonlocal msg
#         msg = "Hello"
#     inner()
#     print(msg)
# outer()