#---------  Decorator


# def decorator(func):
#     def wrapper():
#         print("Before calling function")
#         func()
#         print("After Calling function")
#     return wrapper
# @decorator
# def greet():
#     print("hello")
# greet()




#------- Vowels Check with Decorator


# def decorator(func):
#     def wrapper(text):
#         vowels = "aeiouAEIOU"
#         count = 0
#         for ch in text:
#             if ch in vowels:
#                 count += 1
#         print("Vowel Count" , count)
#         func(text)
#     return wrapper
# @decorator
# def show(text):
#     print("Word is", text)
# show("Programming")
# show("Sinan")
# show("MOhamed Sinan")
# show("SOnakns")




#---------- decorator with argument

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @decorator
# def mul(a,b):
#     return a * b
# print(mul(2,5))
# print(mul(3,5))
# print(mul(6,2))




#------- Convert str into upper


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
# @decorator
# def greet(name):
#     return f"Hello, {name}"
# print(greet("sinan"))



#----- reverse String


def decorator(func):
    def wrapper()