import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    
    def print(self, parent):
        result = 0
        file_out = open('output.txt','a')
        file_out.write("Ребро \tВес\n")
        print("Ребро \tВес")
        for i in range(1, self.V):
            file_out.write(f"{parent[i]},{i}   \t {self.graph[i][parent[i]]}\n")
            print(f"({parent[i]},{i})\t {self.graph[i][parent[i]]}", sep='')
            result += self.graph[i][parent[i]]
        print(f"MST = {result}")

    
    def minim_key(self, key, array_of_MST):
        minim = sys.maxsize
        for v in range(self.V):
            if key[v] < minim and array_of_MST[v] == False:
                minim = key[v]
                min_index = v
        return min_index
    
    def Prim(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        array_of_MST = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minim_key(key, array_of_MST)
            array_of_MST[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and array_of_MST[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.print(parent)

    

file_inp = open('input.txt', 'r')
matrix = []
while True:
    line = file_inp.readline()
    line = line.replace('\n','')
    matrix.append(line)
    if not line:
        break
file_inp.close()

matrix.remove("")

graf = []
for i in range(0, len(matrix)):
    graf.append(matrix[i].split())
for i in range(0, len(graf)):
    for j in range(0, len(graf[i])):
        graf[i][j] = int(graf[i][j])
        
g = Graph(len(graf))
g.graph = graf
g.Prim()



	

