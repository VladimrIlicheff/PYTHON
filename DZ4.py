#  Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

num = int(input('Введите число: '))
new_list = list(range(-num, num+1))
print(new_list)
a = int(input('Введите № 1го числа: '))
b = int(input('Введите № 2го числа: '))
if a <= ((num*2)+1) and b <=((num*2)+1):
   a = new_list[a-1]
   b = new_list[b-1]
   print(a * b)
else: 
    print("There are no values for these indexes!")

     



