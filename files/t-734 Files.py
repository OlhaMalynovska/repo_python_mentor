# У вхідному файлі записано два цілих числа, які можуть бути розділені пропусками і кінцями рядків.
# Виведіть у вихідний файл їх суму.

with open('input2.txt', 'r') as file:
    data = file.read().split()
     print(int(data[0])+int(data[1]))


with open('input2.txt', 'r') as file:
    a, b = map(int, file.read().split())
    print(a + b)
