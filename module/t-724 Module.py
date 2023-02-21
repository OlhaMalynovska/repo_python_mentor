#
# Напишіть програму для перемішування та друку введеної послідовності. Використайте модуль random.
# Вхідні дані:
# Yellow Pink Green Red Black White
# Вихідні дані:
# Pink Yellow White Green Black Red
import random

 string = "Yellow Pink Green Red Black White"
 list_1 = string.split()
 random.shuffle(list_1)
 print(list_1)


# words = 'Yellow Pink Green Red Black White' #your lists as a list of lists
# #picks a list randomly


s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

listToStr = ' '.join([str(elem) for i, elem in enumerate(s)])

print(listToStr)
if __name__ == "__main__":
    main()

# listToStr = ' '.join([str(elem) for i, elem in enumerate(s)])
#
# print(listToStr)
