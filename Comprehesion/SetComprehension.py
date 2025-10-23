
#--------------------------------- Set Comprehension -------------------------------------------


# number = [1,2,2,2,3,3,4,4,5,5,6,7,7,8,9]                    # Creating a simple set
# unique = {n for n in number}
# print(unique)



# number = [1,2,3,4,5]                                        # Find Sqaure
# square = {n**2 for n in number}
# print(square)



# number = [1,1,2,2,2,3,3,4,4,5,6,6,7]                        # Filtering items
# even = {n for n in number if n % 2 == 0}
# print(even)



# matrix = [[1,2],[2,2,2],[2,3,4,5],[3,4,4,5,5,6]]            # Nested loop comprehension
# unique = {n for row in matrix for n in row}
# print(unique)



# number = [1,2,3,4,5]                                          # Conditional expression inside comprehension
# labels = {"Even" if n % 2 == 0 else "Odd" for n in number}
# print(labels)