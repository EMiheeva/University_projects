def find_set(i): 
    while parent[i] != i:
        i = parent[i]
    return i

def union_sets(i, j): 
    parent[find_set(i)] = find_set(j)
    
def kruskal(cost):
    out = open('output.txt','a')
    min_weight = 0
    count = 0
    while count < roots - 1:
        minim = INF
        a = -1
        b = -1
        for i in range(roots):
            for j in range(roots):
                if find_set(i) != find_set(j) and cost[i][j] < minim:
                    minim = cost[i][j]
                    a = i
                    b = j
        union_sets(a, b)
        out.write('Ветвь {}:({},{}), его вес = {}\n'.format(count, a, b, minim))
        print('Ветвь {}:({},{}), его вес = {}'.format(count, a, b, minim))
        count += 1
        min_weight += minim
    out.write("Минимально покрывающее дерева = {}".format(min_weight))
    print("Минимально покрывающее дерева = {}".format(min_weight))
    out.close()
    
inp = open('input.txt', 'r')
matrix = []
while True:
    line = inp.readline()
    line = line.replace('\n','')
    matrix.append(line)
    if not line:
        break
inp.close()

graf = []
for _ in range(0, len(matrix)-1):
    graf.append([])
    
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if(matrix[i][j]!="i"):
            graf[i].append(int(matrix[i][j]))
        else:
            INF = float('inf')
            graf[i].append(INF)
            
roots = len(graf) 
parent = [i for i in range(roots)]

kruskal(graf)
