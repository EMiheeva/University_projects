INF = float('inf')
inp = open("input.txt", "r") 
line = inp.readlines() 
inp.close()

n = len(line)
print(f"В графе из input.txt {n} вершин")
first_edge = int(input("Введите вершину, с которой начать отсчет расстояний: "))
matrix = [] 
for i in range(0, n):
    row = list(line[i].replace('inf', str(INF)).split())
    matrix.append(row) 

def Dijkstra():
    distance = [INF] * n 
    visited = [False] * n 
    distance[first_edge] = 0
    priority_queue = [first_edge] 
    
    while priority_queue: 
        edge_min_dist = min(priority_queue, key=lambda k: distance[k]) 
        priority_queue.remove(edge_min_dist) 
        visited[edge_min_dist] = True 
        for edge in range(0, n): 
            if not visited[edge]: 
                if distance[edge] > distance[edge_min_dist] + float(matrix[edge_min_dist][edge].replace('i', str(INF))): 
                    distance[edge] = distance[edge_min_dist] + float(matrix[edge_min_dist][edge].replace('i', str(INF))) 
                if edge not in priority_queue: 
                    priority_queue.append(edge) 
    
    return distance

result_distance = Dijkstra()

out = open('output_Dijkstra.txt', 'a')
out.write(f"Кратчайшие пути\n")
print(f"Кратчайшие пути")
for i in range(0, n): 
    if ( i == first_edge ):
        print(f"от вершины {first_edge} до вершины {i}:   не существует, это петля")
        out.write(f"от вершины {first_edge} до вершины {i}:   не существует, это петля\n")
    elif (result_distance[i] == INF):
        print(f"от вершины {first_edge} до вершины {i}:   не существует, т.к. бесконечность")
        out.write(f'От вершины {first_edge} до вершины {i}: не существует, т.к. бесконечность\n')
    elif ( i != first_edge ):
        print(f"от вершины {first_edge} до вершины {i}:   {result_distance[i]}")
        out.write(f"от вершины {first_edge} до вершины {i}:   {result_distance[i]}\n")
out.close()
print()

print("Матрица графа из input.txt")
for k in range(n):
    for m in range(n):
        print(str(matrix[k][m]), end=" ")
    print()
print()
print("Результат работы Дейкстры")
for c in range(n):
    print(f"result_distance[{c}] = {str(result_distance[c])}")
print()
