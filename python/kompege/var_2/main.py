
import ipaddress
import pathlib
import fnmatch
from itertools import product
root = str(pathlib.Path(__file__).parent)

# 1 answ: 76

# 2 
# print('w x y z | F')
# for w in range(0,2):
#     for x in range(0,2):
#         for y in range(0,2):
#             for z in range(0,2):
#                 f = y and (x or z) or not(y or z) or w
#                 if (f == 0):
#                     print(f"{w} {x} {y} {z} | {f}")
# answ: xywz

# 3 скипаем
# 4 10001

# 5
# def f(N):
#     n = bin(N)[2:]
#     if (N % 5 == 0):
#         n = n[0:3] + n 
#     else:
#         n += bin((N % 5) * 5)[2:]
#     return int(n, 2)

# for i in range(1, 100000, 2):
#     if (f(i) < 313):
#         print(i, f(i))
# answ: 35

# 6 скипаем

# 7
# i = (2 * 60 * 60 * 25600) / (3840 * 2160)
# N = 2**23
# print(i, N)
# answ: 8388608

# 8
# letters = list('ЛЮСТРА')
# count = 0
# for combo in product(letters, repeat=5):
#     if (''.join(combo).count('Ю') <= 2):
#         count += 1
# print(count)
# answ: 7500

# 9 скипаем
# 10 скипаем

# 11
# a = (20 * 2**13) / (6*12 + 28*2**3)
# print(a)
# answ: 553

# 12
# def f(x):
#     while '33333' in x or '1111' in x:
#         if '33333' in x:
#             x = x.replace('33333', '111')
#         else:
#             x = x.replace('111', '33')
#     return x
# print(f(111*'3'))
# answ: 1113333

# 13
# def count(network):
#     f = int(network.network_address) + 1
#     l = int(network.broadcast_address)
#     count = 0
#     for ip in range(f, l):
#         if (bin(ip)[-8:].count('0') % 3 != 0):
#             count += 1
#     return count

# network = ipaddress.IPv4Network('123.222.111.192/255.255.255.248', strict=False)
# print(count(network))
# answ: 6

# 14
# digits = list('0123456789ABCDEFGHIJKLMN')
# for x in digits:
#     a = int(f"12{x}734", 24) + int(f"8{x}95{x}3", 24) + int(f"24{x}796", 24)
#     if (a % 23 == 0):
#         print(a, a / 23)
# answ: 4166339

# 15
# M = range(32, 69)
# N = range(54, 77)
# result = []
# last = 0
# for c_x in M:
#     for c_y in N:
#         for x in range(1, 100):
#             A = range(c_x, c_y+1)
#             a = not(x in M or x in N) == x not in A
#             if (a == True and last == 0):
#                 last = c_y - c_x
# print(last)
# answ: 22

# 16
# def F(n):
#     if (n < 5): return 4**4
#     if (n > 4):
#         return 4 * F(n - 4) + 4
# print(F(4048))
