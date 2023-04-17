import numpy as np
import math
i = math.inf
g = np.array([[i, 14, 55, 7, 5],
             [8, i, 5, 46, 36],
             [31, 15, i, 29, 6],
             [37, 5, 6, i, 22],
             [6, 25, 31, 38, i]])
# g = np.array([[i, 12, 22, 28, 32],
#              [12, i, 10, 40, 20],
#              [22, 10, i, 50, 10],
#              [28, 27, 17, i, 27],
#              [32, 20, 10, 60, i]])
n = len(g)
res = [] # ребра, входящие в минимальный маршрут
length = 0 # длина пути
s = [x for x in range(n)] # порядок строк в исходной м. смежности, будет изменятся по мере удаления строк и столбцов
c = [x for x in range(n)] # номера столбцов

# функция нахождения замыкания, т.е. ребра, которое нужно взять за бесконечность
def chain(res):
    p = []
    for i in range(len(res)):
        for j in range(2):
            p.append(res[i][j])
    for s in p:
        if p.count(s) == 2:
            p.remove(s)
            p.remove(s)
    return (p[-2], p[-1])

for iter in range(n-1):
    print(g)
    n = len(g)
    for i in range(n):
        length += min(g[i, :])
        g[i, :] -= min(g[i, :]) # минимумы по строкам
    for i in range(n):
        length += min(g[:, i])
        g[:, i] -= min(g[:, i]) # минимумы по столбцам

    # нахождение макс степени 0
    max_del = -math.inf
    stroka = 0
    column = 0
    for i in range(n):
        for j in range(n):
            if g[i, j] == 0:
                if i == 0: a1 = min(g[i+1:, j])
                else: a1 = min(list(g[:i, j]) + list(g[i+1:, j]))
                if j == 0: a2 = min(g[i, j+1:])
                else: a2 = min(list(g[i, :j]) + list(g[i, j+1:]))
                a = a1 + a2
                if a > max_del:
                    max_del = a
                    stroka = i
                    column = j

    s0 = s[stroka] # переход из текущей матрицы в индексы исходной
    c0 = c[column] # т.е. смотрим, кто такая ваша максимальная степень 0 в исходной матрице (n*n)
    res.append((s0, c0))
    # поиск замыкания
    s0 = chain(res)[0]
    c0 = chain(res)[1]
    if c0 not in s or s0 not in c:
        s0 = chain(res)[1]
        c0 = chain(res)[0]
    # переход к текущей матрице и присвоение нужному ребру значение бесконечности
    g[s.index(c0), c.index(s0)] = math.inf
    # удаление строки и столбца, соответствующей максимальной степени 0
    g = np.delete(g, stroka, 0)
    g = np.delete(g, column, 1)
    s.pop(stroka)
    c.pop(column)
print('Длина маршрута: ', length)
print('Ребра, образующий минимальный маршрут', *res)