# 1 вариат kompege

# 1 answ: 35

# 2
# print(f"w x y z | F")
# for w in range(0,2):
#     for x in range(0,2):
#         for y in range(0,2):
#             for z in range(0,2):
#                 F = (y <= x) and not(w) and z
#                 if (F == 1):
#                     print(f"{w} {x} {y} {z} | {F}")
# answ: xwyz

# 3 скипаем
# 4 answ: 8

# 5 
# def F(N):
#     n = bin(N)[2:]
#     s = sum(int(x) for x in n if x.isdigit())
#     if (s % 2 == 0):
#         n += '11'
#     else:
#         n += '01'
#     return int(n, 2)

# for i in range(0, 1000):
#     z = F(i)
#     if (z > 61):
#         print(z)
#         break
# answ: 63

# 6 скипаем

# 7 
# i = 16000 * 2 * 51 * 26 * 60
# t = i / (2**26)
# print(t)
# answ: 37

# 8 
# from itertools import product
# word = 'СЕНТЯБРЬ'
# letters = sorted(word)
# count = 1
# for combo in product(letters, repeat=5):
#     if ((combo[0] == 'Р') and ('Ь' not in combo)) and (count % 2 == 0):
#         print(''.join(combo), count)
#     count += 1
# answ: 16384

# 9 скипаем
# 10 скипаем

# 11
# n = 12 * 256 * 2 ** 16
# n /= 2 ** 23
# answ: 24

# 12
# def F(n):
#     while '22222' in n or '9999' in n:
#         if '22222' in n:
#             n = n.replace('22222', '99')
#         else:
#             n = n.replace('9999', '29')
#     return n

# goal = '9'*68
# result = F(goal)
# answ: 17

# 13
# import ipaddress
# def count_no_dis_5(network):
#     f = int(network.network_address) + 1
#     l = int(network.broadcast_address)
#     return sum(bin(ip).count('1') % 5 != 0 for ip in range(f, l))

# network = ipaddress.IPv4Network('228.172.236.0/255.255.240.0', strict=False)
# print(count_no_dis_5(network))
# answ: 3379

# 14
# def trans(n, base):
#     dig = "0123456789ABCDEFGHIJKLMNOP"
#     n = int(n)
#     if (n == 0): return "0"
#     result = []
#     while(n > 0):
#         result.append(dig[n % base])
#         n = n // base
#     return ''.join(reversed(result))

# a = 4**644 + 4**322 + 16**35 - 64**3
# i = trans(a, 4)
# answ: 61

# 15
# def check(A):
#     for x in range(1, 100):
#         for y in range(1, 100):
#             a = x <= 19 or y < 2*x + A - 50 or y > 17
#             if (not(a)): return False
#     return True

# for i in range(1, 100):
#     if (check(i)):
#         print(i)
#         break
# answ: 28

# 16
# def F(n):
#     if (n > 400): return n**n
#     if (n <= 400): return n + 6 + F(n + 12)
# print(F(72) - F(108))
# answ: 270

# 17
# import pathlib
# pathfile = str(pathlib.Path(__file__).parent) + '/17.txt'
# f = open(pathfile)
# data = [int(x) for x in f]

# def check(glist):
#     if (glist[0] % 77 + glist[1] % 77 == min(data)):
#         return True
#     return False

# result = []
# count = 0
# for x in data:
#     if (count < len(data) - 1):
#         if (check([data[count], data[count+1]])):
#             result.append(sum([data[count], data[count+1]]))
#     count += 1
# print(len(result), max(result))
# 35 186613

# 18 скипаем

# 19 answ: 25
# 20 answ: 13 23
# 21 answ: 21

# 22 скипаем

# 23
# def f(n, b):
#     if (n > b): return 0
#     if (n == 22): return 0
#     if (n == b): return 1
#     return f(n+3, b) + f(n+4, b)
# print(f(16, 38))
# answ: 16

# 24
# import pathlib
# filename = str(pathlib.Path(__file__).parent) + '/24.txt'
# f = open(filename).read()
# len_f = len(f) - 1
# result = []
# count = 0
# count_len = 0
# for i in f:
#     if (count < len_f):
#         if ((i == '+' or i == '*') and (f[count+1] == '+' or f[count+1] == '*')):
#             result.append(count_len)
#             count_len = 0
#         else:
#             count_len += 1
#         count += 1
# print(max(result))
# answ: 190

# 25
import fnmatch
def check(n):
    if fnmatch.fnmatch(str(n), '21?3*145?5'):
        return True
    return False

for i in range(0, 10**10 + 1, 2025):
    if (check(i)):
        print(f"{i} | {i/2025}")
