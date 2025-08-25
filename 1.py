
#-------------------------------------------- list ------------------------------------------------


# n = ["apple", "mango", "banana"]
# n.append("grape")        #  Add to last
# print(n)

# n.insert(1,"orange")     #  Add to any index
# print(n)

# n.extend(["kiwi","pappaya"])    #  Add Multiple items
# print(n)

# n.remove("grape")        #  Remove with name
# print(n)

# n.pop()                  #  Remove last item 
# print(n)

# n.sort()                 #  Sorting items
# print(n)

# n.reverse()              #  Reversing items
# print(n)

# print(len(n))            #  Length of items

# for item in n :          #  Looping
#     print(item)

# if "apple" in n :        #  Checking
#     print("Founded")
# else :
#     print("Not Found")





#-------------------------------------------- Tuple ------------------------------------------------


# n = ("red",10, 1.29, True)
# print(n)

# n="sinan"                        #  packing
# a=19
# p="India"
# pack = n , a, p 
# print(pack)

# un = ("sinan",19,"India")        #  Unpacking
# n, a, p = un
# print(n)
# print(a)
# print(p)






#------------------------------------------ Range -------------------------------------------



# for i in range(10,1,-1):
#     print(i)

# for i in range(1,21):
#     if i == 15:
#         break
#     if i % 3 == 0 :
#         continue
#     print(i, end=" ")




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





#------------------------------------------ Set -------------------------------------------



# n = {1,2,3,4,5,5,6,7,8}              #  Remove Duplicates
# print(n)

# n.add(9)                             #  Adding Single item
# print(n)

# n.update([10,11])                    #  Adding Multiple item
# print(n)

# n.remove(9)                          #  Remove if no value error occur
# print(n)

# n.discard(10)                        #  Removing but no value it not erroe
# print(n)

# n.pop()                              #  Removing random element
# print(n)

# n.clear()                            #  Clear all and empty set
# print(n)

# evenSqr = {x*x for x in range(1,11) if x % 2 == 0}     #  Comprehension
# print(evenSqr)


#------ mathematic Set Operations


# a = {1,2,3}                                 #  Union Combining set & Remove duplicate
# b = {2,3,4,5}
# res = a | b 
# print(res)

# a = {1,2,3}                                 #  Insertion find common element
# b = {2,3,4,5}
# res = a & b
# print(res)

# a = {1,2,3}                                 #  Differnce it check element in a but not in b
# b = {2,3,4,5}
# print(a - b)

# a = {1,2,3}                                 #  Symmetic both dot have element
# b = {2,3,4,5}
# print(a ^ b)

# a = {1,2,3}                                 #  Subset all elemnts of a are in b
# b = {2,3,4,5}
# print(a <= b)

# a = {1,2,3}                                 #  Superset all elements of b are in a
# b = {2,3,4,5}
# print(a >= b)






#------------------------------------------ String -------------------------------------------



# n = ["Hello", "World" , "Python", "is", "Good"]            #  Join
# print(" ".join(n))

# n = "Sinan"                                                #  UpperCase
# print(n.upper())

# n = "sinan"                                                #  Length
# print(len(n))

# n = "SINAN"                                                #  LowerCase
# print(n.lower())

# n = "sinan"                                                #  Stating letter Capital
# print(n.title())

# n = "    Sinan    "                                        #  Starting and ending space removing
# print(n.strip())

# n = "I Love React"                                         #  Replacing item
# print(n.replace("React", "Python"))

# n = "One, Two, Three"                                      #  Spliting 
# print(n.split(","))

# n = "Sinan"                                                #  Startwith and Endwith checking
# print(n.startswith("Si"))
# print(n.endswith("an"))

# n = "sinan"                                                #  How many Count items
# print(n.count("n"))

# n = "python21"                                             #  Check aphabet,number,sapce,lower,etc...
# print(n.isalpha())
# print(n.isalnum())
# print(n.isspace())
# print(n.islower())





