# Напишіть програму для перевірки існування файла в поточному каталозі. Використайте модуль os
from os import path


def main():
    print("File exists:" + str(path.exists('t-720 Module.py')))
    print("File exists:" + str(path.exists('720 Module.py')))


if __name__ == "__main__":
    main()
