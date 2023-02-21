# Напишіть програму для обчислення найменшого спільного кратного (LCM)
# двох натуральних чисел. Використайте модуль fractions.
# Note that the specifications of functions provided in the standard library differ depending on the Python version.


# FYINote that the specifications of functions provided in the standard library differ depending on the Python version.
# Python 3.4 or earlier
# GCD: fractions.gcd() Supports only two arguments)
# Python 3.5 or later
# GCD: math.gcd() (Supports only two arguments)
# Python 3.9 or later
# GCD: math.gcd() (Supports more than three arguments)
# LCM: math.lcm() (Supports more than three arguments

import math

print(math.lcm(15, 17))
