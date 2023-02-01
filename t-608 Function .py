# Напишіть функцію, яка отримує рядок і ціле число n та повертає n копій заданого рядка.

def string_n_times(copy_quantity: int, string_text: str):
    b = copy_quantity
    counter = 0
    while counter <= b:
        print(string_text, end = " ")
        counter += 1


string_n_times(3, 'Let\'s get started! it\'s late ')
