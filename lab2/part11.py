try:
    x = 3 / 0
except Exception as e:
    print('ділення на нуль!')

try:
    x = 2 / 1
except:
    print('ділення на нуль!')
    print('some code...')
