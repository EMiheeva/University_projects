from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list)
    
    def Add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def DFS(self, v, visited):
        visited[v] = True 
        for i in self.graph[v]: 
            if visited[i] == False:
                self.DFS(i, visited)

    def Connection(self):
        visited = [False]*(self.V)

        for i in range(self.V):
            if len(self.graph[i]) != 0:
                break

        if i == self.V - 1:
            return True
        
        self.DFS(i, visited)

        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True
    
    def Euler_exist(self):
        if self.Connection() == False:
            return 0
        else:
            count_edge_with_odd_degree = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    count_edge_with_odd_degree += 1
            if count_edge_with_odd_degree == 0:
                return 2 
            elif count_edge_with_odd_degree == 2:
                return 1
            elif count_edge_with_odd_degree > 2: 
                return 0

    def Test(self, GRAPH):
        check_point = self.Euler_exist()
        if check_point == 0:
            print("Граф не Эйлеров")
        elif check_point == 1:
            print("Граф имеет Эйлеров путь(цепь)")
            self.Find_of_path(GRAPH)
        else:
            print("Граф имеет Эйлеров цикл")
            self.Find_of_path(GRAPH)
    
    def Find_of_path(self, graph):
        n = len(self.graph)

        for i in range(len(graph)):
            graph[i] = [int(elem) for elem in matrix_distance_edge[i]]
        
        count_rebra = []
        for i in range(n):
            count_rebra.append(sum(graph[i]))
        
        edge = 0
        countedge_oddcountrebra = 0
        for i in range(n - 1, -1, -1):
            if (count_rebra[i] % 2 == 1):
                countedge_oddcountrebra += 1
                edge = i

        stack = []
        path = []
        current = edge
        """
        Сначала возьмём пустые стек и путь.
        Если все вершины имеют четное число ребер, то начать с любой. 
        Если две вершины имеют нечетное число ребер, то начать с одной из них. 
        Установим флаг для этой текущей вершины.
        Если текущая вершина имеет хотя бы один соседний узел, 
        то сначала найдите этот узел, а затем найдите текущий узел путем обратного отслеживания. 
        Для этого добавьте текущий узел в стек, удалите границу между текущим узлом и соседним узлом, 
        установите значение переменной current для соседнего узла.
        Если у текущего узла нет соседа, добавьте его в path и в стеке 
        задайте значение current для данной вершины.
        Повторять до тех пор, пока стек не опустеет и 
        у текущего узла не будет ни одного соседа.
        """
        
        while (len(stack) > 0 or sum(graph[current])!= 0):
            if (sum(graph[current]) == 0):
                path.append(current)
                current = stack[-1]
                del stack[-1]
            else:
                for i in range(n):
                    if (graph[current][i] == 1):
                        stack.append(current)
                        graph[current][i] = 0
                        graph[i][current] = 0
                        current = i
                        break
        
        for edge_main in path:
            print(edge_main, end = " -> ")
        print(current)

file = open('input.txt', 'r')
input = []
while True:
    line = file.readline()
    line = line.replace('\n','')
    input.append(line)
    if not line:
        break
input.remove("")

matrix_distance_edge = []
graph_from_file = []

for i in range(0, len(input)):
    matrix_distance_edge.append(input[i].split())
    for j in range(len(matrix_distance_edge[i])):
        if(matrix_distance_edge[i][j] == "1"):
            graph_from_file.append([i,j])

for i in range(0, len(graph_from_file)):
    for j in range(1, len(graph_from_file)):
        if(graph_from_file[i][0] == graph_from_file[j][1] and graph_from_file[i][1] == graph_from_file[j][0]):
            graph_from_file[j] = [" "," "]
space = [" "," "]

graph_from_file = list(filter(lambda x: x != space, graph_from_file))
print("Рёбра графа из файла: ", end="")
print(*graph_from_file)

main_graph = Graph(len(matrix_distance_edge))
for i in range(0, len(graph_from_file)):
    main_graph.Add_edge(graph_from_file[i][0], graph_from_file[i][1])
main_graph.Test(matrix_distance_edge)
