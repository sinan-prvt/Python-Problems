
#--------------------------------- Generator Comprehension -------------------------------------------


# number = [1,2,3,4,5]                                        # Simple generator
# gen = (n**2 for n in number)
# print(gen)
# print(list(gen))




# number = range(1,11)                                        # Generator with condition
# even = (n for n in number if n % 2 == 0)
# print(list(even))



# matrix = [[1,2],[3,4],[5,6]]                                # Nested generator
# gen = (num for row in matrix for num in row)
# print(list(gen))



# num = range(1,11)                                           # Conditional expression in generator
# gen = ("Even" if n % 2 == 0 else "Odd" for n in num)
# print(list(gen))


