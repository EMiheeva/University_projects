# помогашка: https://www.programiz.com/dsa/strongly-connected-components
# https://www.programiz.com/dsa/graph-dfs
# сильная компонент связности не может состоять из одной вершины, как в примерах из ссылок
from itertools import groupby
from collections import Counter
from collections import defaultdict
class Graph: 
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list) 
    
    def add_vershina(self, u, v): 
        self.graph[u].append(v)

    def transponirovanie(self): 
        graph = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]: 
                graph.add_vershina(j, i)
        return graph

    def DFS_first(self, v,visited, componenta): 
        visited[v]= True 
        componenta = componenta + str(v)
        for i in self.graph[v]:
            if visited[i]==False:
                componenta = self.DFS_first(i, visited, componenta)
        return componenta
    
    def DFS_second(self, v, visited, stack):
        visited[v] = True 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFS_second(i, visited, stack)
        stack = stack.append(v)
    
    def FIND_SCC(self):
        stack = []
        visited =[False]*(self.V) 
        for i in range(self.V):
            if visited[i]==False:
                self.DFS_second(i, visited, stack)

        reverse_graph = self.transponirovanie()

        visited =[False]*(self.V)
        delete_dublikat = 0
        result_components = []
        result_components.append("")

        while stack:
            i = stack.pop()
            if visited[i] == False:
                result_components[delete_dublikat] = reverse_graph.DFS_first(i, visited,result_components[delete_dublikat])
                result_components.append("")
                delete_dublikat += 1
        result_components.pop()
        
        
        for i in range(0, len(result_components)):
            if len(result_components[i]) == 1:
                print(f"Вершина {result_components[i]} не входит в компоненты")
                result_components[i]=' '
        result_components = list(reversed(result_components))
        
        
        for i in range(0, len(result_components)-1):
            for j in range(i+1, len(result_components)):
                if(result_components[j].find(result_components[i])!= -1):
                    print(f"Вершина {result_components[i]} не входит в компоненты")
                    result_components[i] = ' '
        
        result_components = [element for element, _ in groupby(result_components)]
        delete_dublikat = Counter(result_components)
        for i in range(0, delete_dublikat[' ']):
            result_components.remove(" ")
        return result_components

input = open('inp.txt', 'r')
matrix = []

while True:
    line = input.readline()
    line = line.replace('\n','')
    matrix.append(line)
    if not line:
        break
matrix.remove("")

graph_from_file = []
main_graph = []
for i in range(0, len(matrix)):
    graph_from_file.append(matrix[i].split())
    for j in range(len(graph_from_file[i])):
        if(graph_from_file[i][j] == "1"):
            main_graph.append([i,j])
#print("Граф: ", end="")
#print(*main_graph)
G = Graph(len(graph_from_file))
for i in range(0, len(main_graph)):
    G.add_vershina(main_graph[i][0], main_graph[i][1])
print ("Сильные компоненты связности (SCC) исходного графа:")
print(*sorted(G.FIND_SCC()))
