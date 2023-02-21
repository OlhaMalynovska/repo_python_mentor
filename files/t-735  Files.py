# Запишіть рядки вхідного файла в зворотному порядку у інший файл. Останній
# рядок вхідного файлу обов’язково закінчується символом \n.
with open('output.txt', 'w') as f:
  for line in reversed(list(open("input1.txt"))):
    f.write(line)
