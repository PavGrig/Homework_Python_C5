# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

N = int(input("Введите значение N: "))

def facterial(n):
    if n < 1:
        return 1
    else:
        return n * facterial(n - 1)

print(facterial(N))

def triangular_num(n):
    if n == 1:
        return 1
    else:
        return n + triangular_num(n - 1)

print(triangular_num(N))