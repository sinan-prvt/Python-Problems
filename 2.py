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
#     print(i, end=" ")





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
# largest = 0
# for num in n:
#     if num > largest:
#         largest = num
# print(largest)




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




