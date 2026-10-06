# Лаба 2, 1
aboba = [random.randint(2, 103) for i in range(5)]
print('исходный массив 1:', aboba)

for i in range(len(aboba)):
    mini = i #называем первое(по индексу) число минимальным
    for j in range(i + 1, len(aboba)):#проходимся дальше по числам(ищем самое минимальное)
        if aboba[j] < aboba[mini]:
            mini = j#если число меньше предыдущего минимального, присваеваем ему это значение
    aboba[i], aboba[mini] = aboba[mini], aboba[i]#меняем элементы местами чтобы в начале стояли самые маленькие
print("готовый массив 1:", aboba)

 # Лаба 2, 2
b = [random.randint(0, 100) for i in range(10)]
print('исходный массив 2:', b)

for i in range(len(b)):
    max = i
    for j in range(i + 1, len(b)):
        if b[j] > b[max]:
            max = j
    b[i], b[max] = b[max], b[i]
print("готовый массив 2:", b)

# Лаба 2, 3
p = ["45-23-67", "12-34-56", "78-11-22", "23-45-67", "34-56-78"]
print('исходный массив 3:', b)
for i in range(len(p)):
    min_index = i
    for j in range(i + 1, len(p)):
        if p[j] < p[min_index]:
            min_index = j
    p[i], p[min_index] = p[min_index], p[i]
print("Задание 3:", p)

