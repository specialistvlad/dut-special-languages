x = int(input('x = '))
if 0 < x < 7:
    print('Значення x входить в заданий діапазон, продовжуємо')
    y = 3 * x - 6
    if y < 0:
        print('Значення y від\'ємне')
    else:
        if y > 0:
            print('Значення y додатнє')
        else:
            print('y = 0')
print('x is ' , x)
