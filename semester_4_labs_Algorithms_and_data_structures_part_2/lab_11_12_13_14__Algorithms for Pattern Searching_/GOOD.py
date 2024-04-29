def find_shift_and_border(shift, border, pattern, M):
	i = M
	j = M + 1
	border[i] = j
	while i > 0:
		while j <= M and pattern[i - 1] != pattern[j - 1]:
			if shift[j] == 0:
				shift[j] = j - i
			j = border[j]
		i -= 1
		j -= 1
		border[i] = j

def find_shifts_for_prefix(shifts, border_position, M):
	prefix_border = border_position[0]
	for i in range(M + 1):
		if shifts[i] == 0:
			shifts[i] = prefix_border
		if i == prefix_border:
			prefix_border = border_position[prefix_border]

def search_with_good(pattern, text):
	array_of_shifts = 0
	M = len(pattern)
	N = len(text)
	checking_4 = False
	main_border = [0] * (M + 1)
	main_shift = [0] * (M + 1)

	find_shift_and_border(main_shift, main_border, pattern, M)
	find_shifts_for_prefix(main_shift, main_border, M)

	while array_of_shifts <= N - M:
		j = M - 1
		while j >= 0 and pattern[j] == text[array_of_shifts + j]:
			j -= 1
		if j < 0:
			print(f"Совпадение! Начальный индекс подстроки: {array_of_shifts}")
			checking_4 = True
			array_of_shifts += main_shift[0]
		else:
			array_of_shifts += main_shift[j + 1]
	return checking_4
