def Coloring(adjacency, N):
    result = [-1] * N
    result[0] = 0; 
    available_color = [False] * N 
    for u in range(1, N):   
        for i in adjacency[u]: 
            if (result[i] != -1):
                available_color[result[i]] = True
        new_color = 0 
        while new_color < N:
            if (available_color[new_color] == False):
                break
            new_color += 1
        result[u] = new_color 
        for i in adjacency[u]: 
            if (result[i] != -1):
                available_color[result[i]] = False
    coloring = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"] #отличная идея, если хроматическое число нестрого меньше 7
    
    out = open('output_Coloring.txt', 'a')
    out.write(f"Раскраска графа\n")
    for u in range(N):
        if (result[u]==0):
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[0]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[0]}\n")
        elif (result[u]==1):
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[1]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[1]}\n")
        elif (result[u]==2):
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[2]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[2]}\n")
        elif (result[u]==3):
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[3]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[3]}\n")
        elif (result[u]==4):
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[4]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[4]}\n")
        elif (result[u]==5):
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[5]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[5]}\n")
        else:
            print(f"Вершина {u}: цвет[{result[u]}] - {coloring[6]}")
            out.write(f"Вершина {u}: цвет[{result[u]}] - {coloring[6]}\n")
    print()
    print(f"Хроматическое число: {max(result)+1}")
    out.write(f"Хроматическое число: {max(result)+1}\n")
    out.close()


inp = open('inp.txt', 'r')
matrix = []
while True:
    line = inp.readline()
    line = line.replace('\n','')
    matrix.append(line)
    if not line:
        break
inp.close()
matrix.remove("")

graph_from_inp = []
for i in range(0, len(matrix)):
    graph_from_inp.append(matrix[i].split())
for i in range(0, len(graph_from_inp)):
    for j in range(0, len(graph_from_inp[i])):
        graph_from_inp[i][j] = int(graph_from_inp[i][j])

neibour_edge = [[] for i in range(len(graph_from_inp))]
#neibour_edge = []
#for i in range(0, len(graph_from_inp)):
    #neibour_edge.append([])
for i in range(0, len(graph_from_inp)):
    for j in range(0, len(graph_from_inp[i])):
        if(graph_from_inp[i][j] != 0):
            neibour_edge[i].append(int(j))
            neibour_edge[j].append(int(i))#дополнительное условие, чтобы можно было создать ориентированный граф

print()
print(f"В графе из input.txt {len(graph_from_inp)} вершин")
print()

for i in range(len(neibour_edge)):
    print(f'Вершина {i} имеет соседей: {list(dict.fromkeys(neibour_edge[i]))}') #если граф ориентированный, то мы наблюдаем, что возникают дубликаты!

print()
print("Раскраска графа:")
print()
Coloring(neibour_edge, len(graph_from_inp))
