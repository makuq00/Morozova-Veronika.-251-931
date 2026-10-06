# Лаба 3, 1
def f1(n):
    if n < 1:
        return
    f1(n - 1)
    print(n, end = " ")
f1(7)#пример

# Лаба 3, 2
def f2(A, B):
    print(A, end = " ")
    if A == B:
        return
    if A < B:
        f2(A + 1, B)
    if A > B:
        f2(A - 1, B)
# f2(26, 7)
# f2(17, 34)

# Лаба 3, 3
def f3(N):
    if N==0:
        return 0
    return (N % 10) + f3(N//10)
print(f3(56378))#пример

# Лаба 3, 4
def f4(N, d = 2):
    if N <= 1:
        return
    if d*d > N:#значит оставшийся простой дельтель это само число N
        print(N, end = " ")
        return
    if N % d == 0:#числр d подходит, выводим его, продолжаем рекурсию
        print(d, end = ' ')
        f4(N//d, d)
    else:#проверяем следующий делитель
        f4(N, d + 1)
f4(235)#пример
