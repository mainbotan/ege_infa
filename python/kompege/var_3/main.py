
# Бля, я невероятно устал от всей этой хуйни, но похуй, 3 вариант

# 2
# print("a b c d | F")
# for a in range(0, 2):
#     for b in range(0, 2):
#         for c in range(0, 2):
#             for d in range(0, 2):
#                 F = ((a <= b) == c) or d
#                 if (F == 0):
#                     print(f"{a} {b} {c} {d} | {F}")
# a d b c
# 1 0 1 0 0
# 1 0 0 1 0
# 0 0 1 0 0

# 5
# def from_10(a, base):
#     digits = '0123456789ABCDEFGHIJKLMNOPQRS'
#     res = []
#     while a > 0:
#         res.append(digits[a % base])
#         a //= base
#     return ''.join(reversed(res))
# def sum_dig(n):
#     r = 0
#     for x in n:
#         r += int(x)
#     return r
# def F(N):
#     n = from_10(N, 3)
#     s = sum_dig(n)
#     if (s % 2 == 0):
#         n = '1' + n + '2'
#     else:
#         n = '2' + n + '0'
#     return int(n, 3)
# for x in range(0, 100):
#     z = F(x)
#     if (z > 100):
#         print(f"{x} => {z}")
#         break

# 7
# import math
# video_for_one = 60 * 1920 * 1080
# audio_for_one = 2 * 24000 * 6
# audio_for_one /= 8
# sum_for_one = (video_for_one + audio_for_one) * 60
# sum_for_50 = sum_for_one * 50
# sum_for_50 /= 1024
# print(math.ceil(sum_for_50))
# answ: 364605469

# 8
# from itertools import product
# digits = "ПРЕСТОЛ"
# dig_l = sorted(digits)
# print(dig_l)
# res = []
# for combo in product(dig_l, repeat=5):
#     c = ''.join(combo)
#     last_char = c[-1]
#     if (last_char == 'Е' or last_char == 'О'):
#         sogl_count = c.count('П') + c.count('Р') + c.count('С') + c.count('Т') + c.count('Л')
#         if (sogl_count <= 3):
#             res.append(c)
# print(len(res))
# answ: 3552

# 11
# print((128*4992) / 2**12)
# answ: 156

# 12
# def f(n):
#     while '411' in n or '1111' in n:
#         if '411' in n:
#             n = n.replace('411', '14')
#         if '1111' in n:
#             n = n.replace('1111', '1')
#     return n
# res = []
# for n in range(3, 10001):
#     s = sum_dig(f('4'+n*'1'))
#     res.append(s)
# print(max(res))
# answ: 8

# 13
# import ipaddress