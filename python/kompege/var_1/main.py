# 1 вариат kompege
# 1
print(f"w x y z | F")
for w in range(0,2):
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                F = (y <= x) and not(w) and z
                if (F == 1):
                    print(f"{w} {x} {y} {z} | {F}")
# answ: xwyz
