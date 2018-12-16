# змінні - імена, які прив'язуються до об'єктів
var = 'I am a string'
print(var)
print(type(var)) # type(var) повертає тип об’єкта, на який посилається var
print()
# їх можна прив'язувати до нових значень var = 42
print(var)
print(type(var))
print()
# проте потрібно розуміти, який тип в даний момент може # мати об'єкт і змішувати несумісні типи не можна
a=5
b= 5
print(a + b) # два числа скласти можна
b = '5'
try:
    print(a + b) # число з рядком - ні (отримуємо помилку)
except Exception as e:
    print(e)

x= 2
y= 8
print(x + y) # додавання
print(x + 3)
print(x - y) # віднімання
print(x * y) # добуток
print(x / y) # ділення
print(x // y) # цілочислене ділення
print(x % y) # остача від ділення
print(x ** y) # внесення в ступінь
print(3.2 * 0.8 - 2 * 5 - 3**3) # арифметичний вираз
print(4 ** 0.5) # внесення в ступінь 0.5 – квадратний корінь
z = -2
print(abs(z)) # модуль числа print(pow(z, 2), z ** 2) # квадрат числа
m = 3.6687656
print(round(m), round(m, 5)) # округлення числа до цілого і до п’яти знаків після коми

import math # імпортуємо модуль math
x = 3.265
PI = math.pi
NUMBER_E = math.e
CONST = 5
print(CONST)
CONST = 10
print(CONST)

# ціле число, найближче ціле знизу, найближче ціле зверху print(math.trunc(x), math.floor(x), math.ceil(x))
print(PI) # константа Пі print(NUMBER_E) # число Eйлера
y = math.sin(PI / 4) # math.sin – синус
print(round(y, 2))
y = 1 / math.sqrt(2) # math.sqrt – квадратний корінь print(round(y, 2))

# логічні операції
print('and:')
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print('or:')
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print('not:')
print(not False)
print(not True)

# логічні вирази
a = True
b = False
c = True
f = a and not b or c or (a and (b or c))
print(f)

a = 2
b = 5
print(a < b)
print(b > 3)
print(a <= 2)
print(b >= 7)
print(a < 3 < b)
print(a == b)
print(a != b)
print(a is b)
print(a is not b) # a и b – різні об'єкти (хоча значення їх можуть бути рівні)
