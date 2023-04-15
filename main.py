import os
from sys import argv

try:
    path = argv[1]
except:
    print('Вы не ввели директорию.')
    exit()

c = input('Вывести размер в одинаковых(Y) или сформатированных(N) размерах: ')
if c == 'Y' or c == 'N':
    print('Начинаем работу!')
else:
    print('Вы ввели неверное занчение. Завершение программы.')
    exit()

files = [f for f in os.scandir(path) if f.is_file()]

files = sorted(files, key=lambda f: os.path.getsize(f), reverse=True)


for f in files:
    if c == 'Y':
        print(f.name, os.path.getsize(f), "байт")
    elif c == 'N':
        if os.path.getsize(f) < 1024 - 1:
            size = f.name + ' ' + str(os.path.getsize(f)) + " байт"
        elif os.path.getsize(f) < 1024*1024 - 1:
            size = f.name + ' ' + str(int(os.path.getsize(f)/1024)) + " килобайт"
        elif os.path.getsize(f) < 1024*1024*1024 - 1:
            size = f.name + ' ' + str(int(os.path.getsize(f)/1024/1024)) + " мегабайт"
        elif os.path.getsize(f) < 1024*1024*1024*1024 - 1:
            size = f.name + ' ' + str(int(os.path.getsize(f)/1024/1024/1024)) + " гигабайт"
        print(size)
