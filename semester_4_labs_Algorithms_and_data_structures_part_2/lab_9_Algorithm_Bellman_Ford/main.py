class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, first_edge):
        distance = [float("Inf")] * self.V
        distance[first_edge] = 0
        
        for _ in range(self.V - 1):
            for u, v, weight in self.graph:
                if distance[u] != float("Inf") and distance[v] > distance[u] + weight:
                    distance[v] = distance[u] + weight
        
        for u, v, weight in self.graph:
            if distance[u] != float("Inf") and distance[v] > distance[u] + weight:
                print("Отрицательный цикл!")
                return
        self.print_on_screen(distance, first_edge)

    def print_on_screen(self, distance, first_edge):
        out = open('output.txt','a')
        out.write(f"Кратчайшие пути")
        print(f"Кратчайшие пути")
        for i in range(self.V):
            INF = float('inf')
            if (distance[i] == INF):
                print(f"от вершины {str(first_edge)} к вершине {i}:   не существует")
                out.write(f"от вершины {str(first_edge)} к вершине {i}:   не существует")
            elif (i != first_edge):
                print(f"от вершины {str(first_edge)} к вершине {i}:   {distance[i]}")
                out.write(f"от вершины {str(first_edge)} к вершине {i}:   {distance[i]}")
        out.close()
        print()

inp = open('input.txt', 'r')
matrix = []
while True:
    line = inp.readline()
    line = line.replace('\n','')
    matrix.append(line)
    if not line:
        break
matrix.remove("")

graph_from_file = []
for i in range(0, len(matrix)):
    graph_from_file.append(matrix[i].split())
inp.close()

main_graph = Graph(len(graph_from_file))

i = 0
while(i <= len(graph_from_file)-1):
    j = 0
    while(j <= len(graph_from_file[i])-1):
        if graph_from_file[i][j] != "0":
            main_graph.add_edge(i, j, int(graph_from_file[i][j]))
        j += 1
    i += 1

for i in range(len(graph_from_file)):
    main_graph.BellmanFord(i)
