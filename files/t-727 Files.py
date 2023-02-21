# Напишіть функцію, яка друкує випадкове ціле число від n до m включно
import random


def main():
    n = int(input('n='))
    m = int(input('m='))

    print(random.randint(n, m))


if __name__ == "__main__":
    main()
