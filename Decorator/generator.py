#======================== Generator =============================================


# def Count():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# for i in Count():
#     print(i)




#-------------------------

def Counter():
    n = 1
    while True:
        yield n
        n += 1
gen = Counter()
for i in range(5):
    print(next(gen))