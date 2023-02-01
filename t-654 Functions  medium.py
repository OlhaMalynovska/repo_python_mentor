# Напишіть функцію для визначення, чи рік високосний чи ні.
def vysokosnyj_year(year:int):
    if year%4 == 0 and year%100 != 0:
        print(f'{year} є високосним роком ')
    elif year%400 == 0:
        print (f'{year} є високосним роком ')
    else:
        print (f'{year} не є високосним роком ')
vysokosnyj_year(2000)