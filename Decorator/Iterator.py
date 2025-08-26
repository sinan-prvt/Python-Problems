#=========================== Iterator =================================


# num = [1,2,3,4,5]
# it = iter(num)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))





#--------------


# class Counter:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current <= self.n :
#             val = self.current
#             self.current += 1
#             return val
#         else:
#             raise StopIteration
# nums = Counter(5)
# for i in nums:
#     print(i)


