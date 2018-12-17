response = input('y/n da/net yes/no да/нет так/ні >>> ').lower().replace(' ' , "")

if response == 'y' or response == 'yes' or response == 'da' \
or response == 'tak' or response == 'да' or response == 'так':
    print('-----')
    print("Вы выбрали сторону добра!")
elif response == 'net' or response == 'n' or response == 'no' \
or response=='нет' or response == 'ні':
    print('-----')
    print("Вы выбрали сторону зла((((!")
else:
    print('грайте ще!')
