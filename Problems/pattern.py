# Pattern Printing in Python


# ========================== Centered Symmetric Cumulative Number Pyramid ================================


# n = 5

# for i in range(1, n+1):
#     for s in range(n - i):
#         print("   ", end="")
    
#     start = i * (i + 1) // 2
    
#     num = start
    
#     for j in range(i):
#         print(f"{num:2d}", end=" ")
#         num -= 1

    
#     if i != 1:
#         num += 1
#         for j in range(i):
#             print(f"{num:2d}", end=" ")
#             num += 1
            
#     print()





# ========================== Concentric Number Box ================================


# n = 4
# size = 2 * n - 1

# for i in range(size):
#     for j in range(size):
#         value = n - min(i, j, size-1-i, size-1-j)
#         print(value, end=" ")
#     print()






# ========================== Palindrome Number Pyramid ================================


# n = 4

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")

#     for j in range(i, 0, -1):
#         print(j, end="")
    
#     for j in range(2, i + 1):
#         print(j, end="")

#     print()






# ========================== Row Start is Triangular ================================



# n = 5 

# for i in range(1, n + 1):
#     start = i * (i + 1) // 2
#     for j in range(i):
#         print(start + j, end=" ")
#     print()



# ========================== Row Start is Square ================================


# n = 5

# for i in range(1, n + 1):
#     start = i * i
#     for j in range(i):
#         print(start + j, end=" ")
#     print()




# ========================== Row Start = i(i+1) ================================


# n = 5

# for i in range(1, n + 1):
#     start = i * (i + 1)
#     for j in range(i):
#         print(start + j, end=" ")
#     print()






# ========================== Alternating Mirror Pattern ================================



# n = 5

# for i in range(1, n + 1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()




# ========================== Diamond Number Pyramid ================================



# n = 5

# for i in range(1, n + 1):
#     print("  " * (n - i), end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     for j in range(2, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(n - 1, 0, -1):
#     print("  " * (n - i), end=" ")
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     for j in range(2, i + 1):
#         print(j, end=" ")
#     print()