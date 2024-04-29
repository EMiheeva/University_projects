"""
https://habr.com/ru/articles/191454/
"""
def search_with_Knuth_Morris_Pratt(pattern, text):
	M = len(pattern)
	N = len(text)
	checking_2 = False
	lps = [0] * M
	j = 0
	calculate_longest_prefix_suffix(pattern, M, lps)
	result = calculate_longest_prefix_suffix(pattern, M, lps)
	print(f"Шаблон: {pattern}")
	print(f"Преффикс-функция данного шаблона: {result}")
	i = 0
	while (N - i) >= (M - j):
		if pattern[j] == text[i]:
			i += 1
			j += 1
		if j == M:
			print(f"Совпадение! Начальный индекс подстроки: {str(i-j)}")
			checking_2 = True
			j = lps[j-1]
		elif i < N and pattern[j] != text[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
	return checking_2

def calculate_longest_prefix_suffix(pattern, M, longest_prefix_suffix):
	length = 0
	longest_prefix_suffix[0] = 0
	i = 1
	while i < M:
		if pattern[i] == pattern[length]:
			length += 1
			longest_prefix_suffix[i] = length
			i += 1
		else:
			if length != 0:
				length = longest_prefix_suffix[length-1]
			else:
				longest_prefix_suffix[i] = 0
				i += 1
	return longest_prefix_suffix
