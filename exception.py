#--------------------------------- Exception Handling -------------------------------------------


#------- ZeroDivisionError

# try:                                                      # Basic Example
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divisible by Zero")




# def demo(x,y):                                            #  Advance Example
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("Cannot Divisible By Zero")
#         result = None
#     else:
#         print("Division Successfully")
#     finally:
#         print("Execution Complete")
#     return result
# print(demo(10,0))
# print(demo(10,2))



#------ ValueError

# try:
#     num = int("abc")
# except ValueError:
#     print("Invalid Number")