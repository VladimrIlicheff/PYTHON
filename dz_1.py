# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal
number = Decimal(input("Введите любое число: "  ))
number_format = input("Введите требуемую точность в формате 0.0001:  ")
number = number.quantize(Decimal(number_format))
print(number)