# Напишіть функцію, яка приймає два слова в якості вхідних даних, і надрукуйте найдовше слово.
# Якщо слова мають однакову довжину, то функція повинна надрукувати слова в окремих рядках.

# string = input("Please enter a string ")
# new = string.split( )
# max_length = 0
# max_word = ""
#
# for word in new:
#     if len(word) > max_length:
#         max_length = len(word)
#         max_word = word
#
# print("The longest word in the string is", max_word)

def max_word(two_words: str):
    new = two_words.split()
    max_length = 0
    max_word = ""

    for word in new:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
            print(max_word)
        elif len(word) == max_length:
               print(len(word))
               print(max_length)


max_word('asdfg sdftr')
