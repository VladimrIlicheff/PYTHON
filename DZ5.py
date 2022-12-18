# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
print ("Введите координату Х")
xA = int (input ())
print ("Введите координату У")
yA = int (input ())
print ("Введите координату Х1")
xB = int (input ())
print ("Введите координату У1")
yB = int (input ())
from math import sqrt
result = sqrt(((xB-xA)**2)+((yB-yA)**2))
print (result)