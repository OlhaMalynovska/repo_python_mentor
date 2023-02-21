# Напишіть програму для підрахунку кількості кожного символу у текстовому файлі без врахування регістру
# літер, використавши модуль collections. Для гарного друку використайте модуль pprint.


import collections
import pprint
def main():

   with open('input1.txt', 'r') as file:
     data = file.read().replace('\n', '')
     pprint.pprint(collections.Counter(data))

if __name__ == "__main__":
    main()
