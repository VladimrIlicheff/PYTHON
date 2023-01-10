# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal, getcontext 
number = input("Введите любое число   ")
y = input("Введите точность в формате 1.000, где количество 0 соотвествует количеству знаков после ,  ")
# number = Decimal("num")
getcontext().prec = 80
print(number.quantize('2'))
