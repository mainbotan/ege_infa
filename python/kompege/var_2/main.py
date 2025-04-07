
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

# 3 2801
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

# 9 answ: 13
# 10 answ: 29

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
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def F(n):
#     if (n < 5): return 4**4
#     if (n > 4):
#         return 4 * F(n - 4) + 4
# print(F(4048))
# answ: разобраться в этой хуйне


# 17
# f = open(root+'/17.txt', 'r')
# data = [int(x) for x in f]
# len_goal = len([z for z in data if z>9 and z<100])
# def check(arr):
#     if (int(str(arr[0])[-1]) + int(str(arr[1])[-1]) == len_goal):
#         return True
#     return False
# result = []
# count = 0
# for i in data:
#     if (count < len(data) - 1):
#         if (check([i, data[count+1]])):
#             result.append(i + data[count+1])
#     count += 1
# print(len(result), min(result))
# answ: 243 3614

# 18 скипаем
# 19 answ: 36
# 20 answ: 39 77
# 21 answ: 80
# 22 скипаем

# 23
# def f(n, g):
#     if (n == 24): return 0
#     if (n < g): return 0
#     if (n == g): return 1
#     return f(n-2, g) + f(n-3, g) + f(n//4, g)
# print(f(36, 13))
# answ: 157

# 24
# data = open(root+'/24.txt').read().split('X')
# max = 0
# for i in data:
#     lenI = str(i).count('Y')
#     if (lenI > max):
#         max = lenI
#         res = str(i)
# answ: 91

# 25
# def getSumDivisors(n):
#     res = sum([int(x) for x in range(1, n+1) if n%x==0])
#     return res
# for i in range(1000, 10000):
#     S = getSumDivisors(i)
#     if (str(S)[-2:] == '23'):
#         print(f"{i} | {S}")
# answ: 
# 1681 | 1723
# 1936 | 4123
# 2592 | 7623
# 3025 | 4123
# 6962 | 10623
# 7569 | 11323

# 26
data = [int(x) for x in open(root+'/26.txt', 'r')]
total_count = data[0]
del data[0]
data = sorted(data)
print(data)