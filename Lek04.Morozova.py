import random

#Лаба 4, 1 и 2
m = [random.randint(50, 100) for i in range(20)]
l = [random.randint(1, 1000) for i in range(1000) ]

def y(m):
    if len(m) <=1:
        return m
    x = m[0]
    men = [i for i in m if i < x]
    bol = [i for i in m if i > x]
    return y(men) + [x] + y(bol)

print(y(m))
print(y(l))

Лаба 4, 3
veron = [[random.randint(5, 61) for b in range(5)]for i in range (4)]

def zxc(a):
    if len(a) <= 1:
        return a
    k = a[0][0]
    men = [i for i in a if i[0] < k]
    bol = [i for i in a if i[0] > k]
    return zxc(men) + [a[0]] + zxc(bol)

print(zxc(veron))

Лаба 4, 4
a = [
    "Морозова Вероника",
    "Гетун Ярослав",
    "Простякова Татьяна",
    "Шляндин Кирилл",
    "Макарова Мария",
]
a.sort()

for i in a:
    print(i)
