# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

N = int(input("Введите номер числа Фибоначи: "))

def fib(N):
    if N < 1:
        return print("Число введено не корректно!!!")
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return fib(N - 2) + fib(N - 1)

print(fib(N))