x = int(input('x = '))
if x > 0:
    print("{} > 0 is {}".format(x, x > 0))
    y = x ** 0.5
else:
    y = x ** 2
    print(y)
