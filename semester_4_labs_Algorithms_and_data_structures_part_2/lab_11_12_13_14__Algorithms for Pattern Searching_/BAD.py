"""
https://habr.com/ru/articles/660767/
"""
alphabet = 256 
def Bad_Heuristic(string, size):
	bad_letter = [-1] * alphabet
	for i in range(size):
		bad_letter[ord(string[i])] = i
	return bad_letter

def search_with_bad(pattern, text):
	M = len(pattern)
	N = len(text)
	checking_3 = False
	bad_character = Bad_Heuristic(pattern, M)
	shift = 0
	while(shift <= N-M):
		j = M-1
		while j>=0 and pattern[j] == text[shift+j]:
			j -= 1
		if j<0:
			print(f"Совпадение! Начальный индекс подстроки: {shift}")
			checking_3 = True
			shift += (M - bad_character[ord(text[shift+M])] if shift+M<N else 1)
		else:
			shift += max(1, j - bad_character[ord(text[shift+j])])
	return checking_3
