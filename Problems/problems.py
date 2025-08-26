#----- Reverse "hello" without slicing


# n = "hello"
# rev = ""
# for ch in n:
#     rev = ch + rev
# print(rev)




#----- Count vowels in "programming"


# n = "programming"
# vowels = "aeiou"
# count = 0
# for ch in n:
#     if ch in vowels:
#         count += 1
# print("Vowels Count:", count)



#------ Vowels with *


# word = "Mohamed Sinan"
# vowels = "aeiouAEIOU"
# li = []
# for i in word:
#     if i in vowels:
#         print("*")
#     else:
#         print(i)
# print(" ".join(li))



#------  Check if number is even or odd


# n = 94
# if n % 2 == 0 :
#     print("It Is even Number")
# else :
#     print("It is Odd Number")





#----- Find sum of [1,2,3,4] without sum()


# n = [1,2,3,4]
# total = 0
# for ch in n:
#     total += ch
# print(total)




#----- Print 1–20, skip multiples of 3, stop if number is 15.


# for i in range(1,21):
#     if i == 15:
#         break
#     if i % 3 == 0:
#         continue
# print(i, end=" ")


#----- Access Nested Dictionary


# students = {
#     101 : {"name": "Sinan", "marks": {"math":90, "eng":60}},
#     102 : {"name": "Nishad", "marks": {"math":50, "eng":30}},
#     103 : {"name": "Affan", "marks": {"math":30, "eng":90}},
#     104 : {"name": "Vishnu", "marks": {"math":90, "eng":80}}
# }

# print(students[101]["name"])
# print(students[103]["marks"]["eng"])




#-----Count letters in word


# n = "sinan"
# letters = {}
# for ch in n:
#     if ch in letters:
#         letters[ch] += 1
#     else :
#         letters[ch] = 1
# print(letters)



# n = "sinan"
# freq = {}
# for ch in n:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)



#----Count words in sentence


# n = "Hi My Name Is Sinan And Your Name Also Sinan"
# words = n.split()
# freq = {}
# for ch in words:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)





#-----convert list into dict with even and odd


# n = [1,2,3,4,5,6,7,8,9]
# res = {"even":[] , "odd":[]}
# for num in n :
#     if num % 2 == 0:
#         res["even"].append(num)
#     else :
#         res["odd"].append(num)
# print(res)





#-------Find Largest Number

# n = [3,4,6,8,9]
# largest = num[0]
# for num in n:
#     if num > largest:
#         largest = num
# print(largest)



#------ Find Smallest Number

# num = [1,2,3,4,5,6]
# smallest = num[0]
# for n in num:
#     if n < smallest:
#         smallest = n
# print(smallest)



#------- Find Second Largest Number


# num = [2,3,5,7,8]
# unique = list(set(num))
# unique.sort()
# print(unique[-2])




#------ Check if "madam" is palindrome.


# n = "madam"
# if n == n[::-1]:
#     print("Palindrom")
# else :
#     print("Not Palindrome")





#-------Factorial using Loop


# num = 5
# fac = 1
# for i in range(1, num+1):
#     fac *= i
# print(fac)





#-------- Prime Number 


# for num in range(2,51):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)




#---------- Fibnocci Series


# a, b = 0, 1
# for _ in range(10):
#     print(a)
#     a, b = b, a + b



#-------- Count Digits 

# num = 123456
# count = 0
# while num > 0 :
#     count += 1
#     num //= 10
# print(count)








#------- Remove Duplicates


# num = [1,2,2,3,3,4,4,5,5,3,2,2,1]
# unique = []
# for n in num:
#     if n not in unique:
#         unique.append(n)
# print(unique)





#------------ Reverse Word In String


# s = "Hello My Name Sinan"
# word = s.split()
# rev = " ".join(word[::-1])
# print(rev)






#-------------- Arm Strong Numbers


# num = 153
# digit = [int(d) for d in str(num)]
# total = sum(d**3 for d in digit)
# if total == num:
#     print("It Is a ArmStrong Number")
# else:
#     print("It is not a ArmStrong Number")






#-------------  Multiple Table 


# num = 4
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")






#------------- Anagram Check


# s1 = "silent"
# s2 = "listen"
# if sorted(s1) == sorted(s2):
#     print("It is Anagram")
# else:
#     print("It is not Anagram")





#------------ Substring Check


# s = "Sinan"
# sub = "na"
# if sub in s:
#     print("Founded")
# else:
#     print("Not Founded")





