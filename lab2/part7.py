print('''Меню:
    1. Файл
    2. Вид
    3. Вихід
''')
#
choice = input('Ваш вибір: ')
if choice == '1':
    print('Ви вибрали пункт меню "Файл"')
elif choice == '2':
    print('Ви відкрили меню "Вид"')
elif choice == '3':
    print('Завершення роботи.')
else:
    print('Некоректний вибір')
