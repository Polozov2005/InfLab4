import numpy as np

A = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 0]
]
A = np.array(A)

v = 3

## Определение числа компонент связности
# Объявление списка компонент связности K
K = [[0]]

# Объявление счётчика компонент k
k = 0

# Объявление списка посещённых вершин visited_nodes
visited_nodes = [0]

# Объявление счётчика посещённых вершин n
n = 0

while n != v:
    # Объявление счётчика порядкового номера вершины в k-ой компоненте a
    a = 0
    while a != len(K[k]):
        i = K[k][a]
        for j in range(v):
            if not(j in visited_nodes) and A[i, j] == 1:
                K[k] += [j]
                visited_nodes += [j]
                n += 1
        a += 1
    i = 0
    while i in visited_nodes:
        i += 1
    visited_nodes += [i]
    n += 1
    K += [[i]]
    k += 1
K.pop()
print(K)