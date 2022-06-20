"""Восстановление траектории шахматного коня"""
"""по каким клеткам должен пройти конь, чтобы попасть из d4 в f7 наиболее быстро"""
from collections import deque

def add_edge(v1, v2):
    """Добавляет ребро (возможный шаг коня)"""
    graph[v1].add(v2)
    graph[v2].add(v1)

# Создание (графа) словаря, в котором ключи соответствуют всем ячейкам шахматной доски. Значения - пустые множества.
letters = "abcdefgh"
numbers = "12345678"
graph = dict()
for l in letters:
    for n in numbers:
        graph[l+n] = set()

# Граф заполняется всеми возможными ходами коня для каждой ячейки.
for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i+2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i-2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i+1] + numbers[j+2]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i-1] + numbers[j+2]
            add_edge(v1, v2)

# Словарь расстояний и предков для каждой ячейки
distances = {v: None for v in graph}
parents = {v: None for v in graph}
# Ячейка в которой находится конь и ячейка куда он должен попасть
start_vertex = 'd4'
end_vertex = 'f7'

distances[start_vertex] = 0
# Создание очереди
queue = deque([start_vertex])

# Пока очередь не пуста
while queue:
    # Достаем 1 элемент
    cur_v = queue.popleft()
    # Перебор всех его "соседей"
    for neigh_v in graph[cur_v]:
        # Если "сосед" еще не посещен
        if distances[neigh_v] is None:
            # Считается расстояние
            distances[neigh_v] = distances[cur_v] + 1
            # "Сосед" добавляется в очередь, чтобы перебрать его "соседей"
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

# путь начинает записываться с конца
path = [end_vertex]
parent = parents[end_vertex]
while parent is not None:
    path.append(parent)
    parent = parents[parent]

# Вывод расстояния
print(path[::-1])