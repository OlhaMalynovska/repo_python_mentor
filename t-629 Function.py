# Напишіть функцію для підрахунку суми всіх елементів у списку цілих чисел.
def odd_numbers(a: list):
    summ_of_element = 0
    for element in range(len(a)):
        summ_of_element+=a[element]
    print(f'{summ_of_element}')

odd_numbers([1, 2, 4, 3, 5,5, 7, 6, 8, 9])