# Напишіть функцію, яка повертає зі списку найменше і найбільше числа.
# 61 9 -5 23 15 44 31 10 -14 7 8
def max_min_number(a: list):
    set_first_as_min = a[0]
    for index in range(len(a)):
        if set_first_as_min > a[index]:
            set_first_as_min = a[index]
    set_first_as_max = a[0]
    for index in range(len(a)):
        if set_first_as_max < a[index]:
            set_first_as_max = a[index]
    print(f'{(set_first_as_max, set_first_as_min)}')

max_min_number([2, 5, 6,5,7,8,-9,-87])
