# def myTest():
#     yield 1
#     yield 5
#     yield 6
#     yield 99

# a = myTest()
# b = myTest()

# print(a.__next__())
# print(a.__next__())

# print(b.__next__())
# print(b.__next__())

# print(a.__next__())


# My Own tests
def myTest():
    x = 0
    while x < 10:
        yield x
        x += 1


for a in myTest():
    print(a)
