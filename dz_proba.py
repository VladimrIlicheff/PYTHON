
# def user_input(user_str):
#     new_str = user_str.split()
#     lst = []

#     for i in range(len(new_str)):
#         new_str[i] = new_str[i].strip(",;!")
#     if new_str[i].replace("-", "", 1).isdigit():
#         lst.append(new_str[i])

#     return lst

# def user_output(lst):
#     if lst:
#         return max(lst, key=int), min(lst, key=int)
#     return"Something strange"

# print(user_output(user_input(input("..."))))


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

# from math import sqrt
# def discr(a, b, c):
#     D = b**2-4*a*c
#     with open("diskr.txt", "a", encoding="utf-8") as file: # открытие файла, в скобках - название файла, способ записи, кодировка, за скобками маркер и закрытие файла
#         file.write(f"{a}x² + {b}x + {c} = 0\n")
#         if D > 0:
#             x1 = (-b+sqrt(D))/(2*a)
#             x2 = (-b-sqrt(D))/(2*a)
#             file.write(f"{x1}, {x2}\n")
#         elif D == 0:
#             x = -b/(2*a)
#             file.write(f"{x}\n")
#         else:
#             file.write("Нет корней\n")
# discr(2, 3, 1)
# # 3. На вход программе подается число n.
# # Программа печатает численный треугольник.
# # Используем вложенные циклы.
# number = int(input())
# for i in range(1, number+1):
#     for k in range(i):
#       print(i, end="")
# print()

my_list = ['Python', 'C++', 'C#', 'Java', "Java", 'C++']


my_set = set(my_list)
New_List=list(my_set)

print("Уникальным значениями в списке {0} являются".format(my_list))

for i in New_List:
  print(i)