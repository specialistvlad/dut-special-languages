# числа в десятковій системі числення
dec1 = 8
dec2 = 42
dec3 = -3
dec4 = 25802836572356723058203845293402834028304820938402834023580235777082489436236
print(type(dec1))
print(dec2)
print(dec3)
print(type(dec4))
print()
"""
block comment
"""

# числа в шістнадцятиричній системі числення
hex1 = 0x9
hex2 = 0xA
hex3 = 0xFF
hex4 = 0x3de
print(hex1)
print(hex2)
print(hex3)
print(hex4)
print()

# число в двійковій системі числення
bin1 = 0b11101101
print(bin1)
print()

#число в восьмеричній системі числення
oct1 = 0o765
print(oct1)

# # ціле число з іншого значення
string = "15"
print(type(string))
number = int(string)
print(type(number))
print(number)
print(number + 5)
try:
    print(string + 5) #-- помилка
except Exception as e:
    print(e)

# істинне значення
bool1 = True
# неправдиве значення
bool2 = False
print(type(bool1))
print(bool2)

# приклади дійсних чисел
a = .5123
b = 3.2
# приклади дійсних чисел в експоненційній формі запису
c = 3.2e5 # 3.2 * 10**5
d = 1e-3 # 1 * 10**(-3)
print(a, b)
print(c, d, sep='---')
# створення дійсного значення some_float_var = float("0.5") print(type(some_float_var)) # зі строки print(float(3)) # з цілого числа

# приклади комплексних чисел
c1 = 2 + 3j # 2 + 3i, 2 – дійсна частина, 3 – уявна частина
c2 = 5 - 5j # 5 - 5i
c6= 5 + 1j
# побудова комплексного числа з дійсних чисел
a=2
b =3
c3 = complex(a, b)
c4 = complex(5, -5)
print(c1, c2 , c6)
print(c3, c4)
print(type(c1))
