"""
Главное в построении конечного автомата — получить следующее состояние из текущего состояния для каждого возможного символа. 
Имея символ x и состояние k, мы можем получить следующее состояние, рассматривая строку «pat[0..k-1]x», 
которая в основном представляет собой конкатенацию символов шаблона pat[0], pat[1] …pat[ k-1] и символ x. 
Идея состоит в том, чтобы из lps данного шаблона получить его максимальную длину так, 
чтобы префикс также был суффиксом «pat[0..k-1]x». Значение длины дает нам следующее состояние. 

Короче, именно с помощью преффикс-функции становится ясно про переход состояний в конечном автомате.
А переход состояний показыает, содержится ли шаблон в тексте.
Этот подход проверяет каждый символ текста ровно один раз, чтобы найти шаблон. 
таким образом, для сопоставления требуется линейное время
https://russianblogs.com/article/6924460187/
"""
alphabet = 256 
def Finite_Automat(pattern, M, table):
	longest_prefix_suffix = 0

	for symbol in range(alphabet):
		table[0][symbol] = 0
	table[0][ord(pattern[0])] = 1

	for i in range(1, M+1):
		for symbol in range(alphabet):
			table[i][symbol] = table[longest_prefix_suffix][symbol]
		if (i < M):
			table[i][ord(pattern[i])] = i + 1
			longest_prefix_suffix = table[longest_prefix_suffix][ord(pattern[i])]

def search_with_FA(pattern, text):
	M = len(pattern)
	N = len(text)
	checking_1 = False
	table = [[0 for i in range(alphabet)] for j in range(M + 1)]
	Finite_Automat(pattern, M, table)
	j = 0
	for i in range(N):
		j = table[j][ord(text[i])]
		if (j == M):
			print(f"Совпадение! Начальный индекс подстроки: {i-M+1}")
			checking_1 = True
	return checking_1
