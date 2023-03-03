"""
https://stepik.org/lesson/680669/step/13?unit=679339


"""
from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]

combs = []
for i in range(21):
    s = combinations_with_replacement(wallet, i)
    for j in s:
        if sum(j) == 100:
            combs.append(j)
print(len(combs))