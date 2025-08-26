
#------------------------------------------ Dicionary -------------------------------------------


# person = {
#     "name" : "Sinan",
#     "age" : 19,
#     "place" : "Kottakkal" 
# }

# person["place"] = "Puthupparamba"         #  Updating
# print(person)

# person["country"] = "India"               #  Adding
# print(person)

# person.pop("place")                       #  Removing
# print(person)

# print(person.keys())                      #  keys print

# print(person.values())                    #  values print

# for key, value in person.items():         #  Looping
#     print(key, ":" , value)

# if "name" in person :                     #  Checking
#     print("Yes it Is in it")
# else :
#     print("No it is not in it")

# sqr = {x: x*x for x in range(1,6)}        #  Comprehension
# print(sqr)


# import copy                                                                 #  Shallow Copy
# org = {"name":"sinan" ,"marks": {"eng": 43, "math":95}}
# shallow = copy.copy(org)
# shallow["marks"]["math"] = 90
# print(org)
# print(shallow)


# import copy                                                                 #  Deep Copy 
# org = {"name":"sinan" ,"marks": {"eng": 43, "math":95}}
# deep = copy.deepcopy(org)
# deep["marks"]["math"] = 98
# print(org)
# print(deep)