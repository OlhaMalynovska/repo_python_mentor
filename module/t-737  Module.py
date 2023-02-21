# Напишіть програму для перевірки, чи містить введений рядок
# усі літери англійського алфавіту. Використайте модуль string, для отримання рядкових констант.

import string

sentance = 'The quick brown fox jumps over the lazy dog'
sentance = sentance.replace(' ','')
print(sentance.isalpha())
