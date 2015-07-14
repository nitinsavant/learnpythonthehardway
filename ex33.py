# def whiletest(testvalue):
#     numbers = []
#     i = 0
#     while i < testvalue:
#         print "At the top i is %d" % i
#         numbers.append(i)
#
#         i = i + 2
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d\n" % i
#     return numbers

def whiletest(testvalue):
    numbers = []
    for num in testvalue:
        numbers.append(num)
    return numbers

numbers = whiletest(range(0,10))

print "The numbers: "

for num in numbers:
    print num
