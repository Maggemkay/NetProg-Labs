def fibonacci():
    x = 1
    y = 0
    while x < 1000000:
        yield x
        x, y = x + y, x
        

for i in fibonacci():
    print(i)
