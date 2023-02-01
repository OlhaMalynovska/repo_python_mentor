# Напишіть функцію для друку парних чисел із заданої послідовності цілих чисел.
def odd_numbers(a: list):
    odd_list = []
    for element in range(len(a)):
        if a[element] % 2 == 0:
            odd_list.append(a[element])
    print(f'{odd_list}')

odd_numbers([1, 2, 4, 3, 5, 5, 4, 6, 8, 10])
