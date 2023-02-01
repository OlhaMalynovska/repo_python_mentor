# Напишіть функцію, яка отримує 3 аргументи: перші 2 - числа, третій - операція (+, -, *, /), яка повинна
# бути проведена над ними. У випадку невідомої операції,
# функція повертає рядок Unknown operation. Результатом має бути дійсне число з двома знаками після десяткової крапки.


def math_oper(number1, number2, operator):
    if operator == '+':
        print(round((number1 + number2), 2))
        return number1 + number2

    elif operator == '-':
        print(round((number1 - number2), 2))
        return number1 - number2
    elif operator == '*':
        print(round((number1 * number2), 2))
        return number1 * number2
    elif operator == '/':
        print(round((number1 /number2), 2))
        return number1 / number2
    else:
        print ('Unknown operation')


math_oper(3, 90, '/')
