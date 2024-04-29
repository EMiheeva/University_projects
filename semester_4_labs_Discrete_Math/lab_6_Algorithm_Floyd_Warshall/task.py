"""
Написать программу, реализующую перевод
матрицы смежности в матрицу инцидентности.
"""

#для невзвенного графа
"""
def adjacency_to_incidence(adjacency_matrix):
    n = len(adjacency_matrix)
    m = sum(sum(adjacency_matrix[i]) for i in range(n)) // 2
    incidence_matrix = [[0] * m for _ in range(n)]
    edge_idx = 0
    for i in range(n):
        for j in range(i+1, n):
            if adjacency_matrix[i][j] != 0:
                incidence_matrix[i][edge_idx] = 1
                incidence_matrix[j][edge_idx] = 1
                edge_idx += 1
    return incidence_matrix
"""

"""
Написать программу, реализующую перевод
матрицы смежности в матрицу инцидентности.
"""
#для взвешенного графа
def adjacency_to_incidence(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    num_edges = sum(sum(adjacency_matrix[i][j]!=0 for j in range(num_vertices)) for i in range(num_vertices))
    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]
    edge_count = 0
    for i in range(num_vertices):
        for j in range(num_vertices):
            weight = adjacency_matrix[i][j]
            if weight != 0:
                incidence_matrix[i][edge_count] = weight
                incidence_matrix[j][edge_count] = -weight
                edge_count += 1
    return incidence_matrix

n = int(input("Введите количество вершин графа(порядок матрицы): "))
adjacency_matrix = []
for i in range(n):
    row = list(map(int, input(f"Введите строку {i+1} матрицы смежности через пробел: ").split()))
    adjacency_matrix.append(row)

"""
Вывод результатов программы на экран
"""

incidence_matrix = adjacency_to_incidence(adjacency_matrix)
print("Первый вид записи")
for row in incidence_matrix:
    print(row)

print()

#print(incidence_matrix)
print("Второй вид записи")
for row in incidence_matrix:
    print(" ".join(str(elem) for elem in row))

print()

"""
Считая граф неориентированным, найти кратчайшие пути между всеми вершинами.
"""

INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    next = [[j if graph[i][j] != 0 else -1 for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    for i in range(n):
        for j in range(n):
            if i != j and next[i][j] != -1:
                path = [i]
                while path[-1] != j:
                    path.append(next[path[-1]][j])
                print(f"Кратчайший путь от вершины {i} до вершины {j}:\n {' -> '.join(map(str, path))} \n")

dist = floyd_warshall(adjacency_matrix)
