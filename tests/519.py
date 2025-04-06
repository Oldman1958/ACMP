"""
Требуется написать программу, которая найдет наименьшее и наибольшее числа, состоящие из тех же цифр, что и заданное
натуральное число N.

Входные данные
Входной файл INPUT.TXT содержит натуральное число N (N ≤ 2×109).

Выходные данные
Выходной файл OUTPUT.TXT должен содержать в одной строке наименьшее, а через пробел – наибольшее числа.
"""
n = list(input())
n_min = sorted(n)
k = n.count('0')
n_min_out = list(n_min[k]) + n_min[:k] + n_min[k + 1:]
n_max = sorted(n, reverse=True)
print(*n_min_out, sep='', end=' ')
print(*n_max, sep='')
