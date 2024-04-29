from collections import defaultdict

# Класс представляет ориентированный граф,
# используя матрицу пропускных способностей
class Graph:

	def __init__(self,graph):
		self.graph = graph # Остаточный граф
		self.org_graph = [i[:] for i in graph]
		self. ROW = len(graph)
		self.COL = len(graph[0])


	''' Поиск в ширину. Возвращает true, если существует путь от
	истока 's' к стоку 't' в остаточном графе. parent[] хранит пути '''
	def BFS(self,s, t, parent):

		# Отметим все вершины не посещенными, это логично
		visited =[False]*(self.ROW)

		# Очередь для поиска в ширину
		queue=[]

		# Отметим текущий узел как посещенный и поставим его в очередь
		queue.append(s)
		visited[s] = True

		while queue:

			# Снимем вершину из очереди 
			u = queue.pop(0)

			# Получим все вершины, инцидентные с текущей вершиной u.
			# Если инцидентная вершина не была посещена, то пометить её
			# посещенной и поставить в очередь
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 :
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u

		# Если мы достигли стока во время поиска в ширину, то возвращаем true
		return True if visited[t] else False
		
	# Обходим граф с помощью поиска в глубину
	def dfs(self, graph,s,visited):
		visited[s]=True
		for i in range(len(graph)):
			if graph[s][i]>0 and not visited[i]:
				self.dfs(graph,i,visited)

	# Отсюда начинается работа алгоритма Форда-Фалкерсона
	def minCut(self, source, sink):

		# Этот массив создан с помощью поиска в ширину и хранит путь
		parent = [-1]*(self.ROW)

		max_flow = 0 # Инициализируем максимальный поток

		# Ищем максимальный поток, пока есть путь от истока к стоку
		while self.BFS(source, sink, parent) :
			# Находим максимальный поток с помощью минимальных пропускных способностей.
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min(path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Добавляем путь к максимальному потоку
			max_flow += path_flow

			# Обновляем пропускные способности ребер 
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]
		#print(f"Максимальный поток: {max_flow}")

		visited=len(self.graph)*[False]
		self.dfs(self.graph,s,visited)
		check = 0
		mass_check = []

		# Выводим ребра, которые первоначально имели вес.
		# но теперь их вес равняется 0 и их, следовательно, можно убрать. Они и будут являться 
                # минимальным разрезом соответствующего максимального потока

		for i in range(self.ROW):
			for j in range(self.COL):
				if visited[i] and not(visited[j]) and self.org_graph[i][j] > 0:
					print(f"Ребро, входящее в минимальный разрез: ({str(i)},{str(j)}), его пропускная способность: {self.org_graph[i][j]}")
					check += self.org_graph[i][j]
					mass_check.append(self.org_graph[i][j])
					#print(f"{check}+{self.org_graph[i][j]}")
		#print(f"Максимальный поток: {check}")
		print(f'Максимальный поток равен: {"+".join(str(x) for x in mass_check)}={sum(mass_check)}')
		

		

"""
# Ввести эту матрицу
graph = [[0, 7, 15, 13, 0, 0, 0, 0], 
        [0, 0, 0, 0, 12, 0, 13, 0], 
        [0, 0, 0, 0, 12, 5, 0, 0], 
        [0, 0, 12, 0, 11, 0, 6, 0], 
        [0, 0, 0, 0, 0, 0, 0, 6], 
        [0, 0, 0, 0, 0, 0, 11, 14], 
        [0, 0, 0, 0, 0, 0, 0, 5], 
        [0, 0, 0, 0, 0, 0, 0, 0]]
"""

n = int(input("Введите количество вершин: "))
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
source = int(input("Введите исток S: "))
sink = int(input("Введите сток T: "))


g = Graph(graph)
g.minCut(source, sink)
