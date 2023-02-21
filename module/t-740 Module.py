# Напишіть програму для перевірки, чи містить введений рядок
# усі літери англійського алфавіту. Використайте модуль string, для отримання рядкових констант.



import datetime as dt

today = dt.datetime.today()

print('Current date and time:', today)

print('Current year:', today.strftime("%y"),

        ' Month of year:', today.strftime("%b"))

print('Week number of the year:', today.strftime("%W"),

         'Weekday of the week:', today.strftime("%w") )

print('Day of year:', today.strftime("%j"), 'Day of the month:',

       today.strftime("%d"), 'Day of week:', today.strftime("%A"))

