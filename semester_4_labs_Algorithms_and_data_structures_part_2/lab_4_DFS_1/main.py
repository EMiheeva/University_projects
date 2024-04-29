from itertools import groupby
from collections import Counter
import functools
def DFS(graph, started_edges, components, n, visited=None):
    if visited is None:
        visited = set()

    visited.add(started_edges)
    print(started_edges, end=" ")
    
    edges = list(started_edges)

    for i in range(0, len(edges)):
        components[n].append(edges[i])

    for next in graph[started_edges] - visited:
        DFS(graph, next, components, n, visited)
    
    return visited

file = open('input.txt', 'r')
input = []
while True:
    line = file.readline()
    line = line.replace('\n','')
    line = line.replace(' ','')
    input.append(line)
    if not line:
        break
file.close()

matrix_distance_edge = []
for _ in range(0, len(input)-1):
    matrix_distance_edge.append([])
for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if(input[i][j] == "1"):
            matrix_distance_edge[i].append(str(j))


graph = {}
graph['0'] = set(matrix_distance_edge[0])
for i in range(0, len(matrix_distance_edge)):
    graph[str(i)] = set(matrix_distance_edge[i])
component_after_dfs = [[],[],[],[],[],[],[],[]]
for i in range(0, len(matrix_distance_edge)):
    DFS(graph, str(i), component_after_dfs, i)
    print("DFS complete")
    print()


COMPONENT = []
for i in range(0, len(component_after_dfs)):
    string_component = ""
    for j in range(0, len(component_after_dfs[i])):
        string_component += component_after_dfs[i][j]
    COMPONENT.append(functools.reduce(lambda x, y: x+y, sorted(string_component)))


for i in range(0, len(COMPONENT)):
    COMPONENT[i] = "".join(set(COMPONENT[i]))
    backup_component = sorted(COMPONENT[i])
    COMPONENT[i]=''.join(backup_component)
for i in range(0,len(COMPONENT)-1):
    for j in range(i+1, len(COMPONENT)):
        if(COMPONENT[j].find(COMPONENT[i])!= -1):
            COMPONENT[i] = " "
COMPONENT = list(reversed(COMPONENT))
for i in range(0,len(COMPONENT)-1):
    for j in range(i+1, len(COMPONENT)):
        if(COMPONENT[j].find(COMPONENT[i])!= -1):
            COMPONENT[i] = " "
COMPONENT = [element for element, _ in groupby(COMPONENT)]
count = Counter(COMPONENT)
for _ in range(0, count[' ']):
    COMPONENT.remove(" ")
COMPONENT = sorted(COMPONENT)

for k in range(0, len(COMPONENT)):
    print(f"Компонента связности номер {k+1}: {COMPONENT[k]} ")
#print(f"Всего компонент связности: {len(COMPONENT)}")
