"""
https://medium.com/nuances-of-programming/%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D1%80%D0%B0%D0%B1%D0%B8%D0%BD%D0%B0-%D0%BA%D0%B0%D1%80%D0%BF%D0%B0-%D1%81-%D0%BF%D0%BE%D0%BB%D0%B8%D0%BD%D0%BE%D0%BC%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC-%D1%85%D0%B5%D1%88%D0%B5%D0%BC-%D0%B8-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B0%D1%80%D0%B8%D1%84%D0%BC%D0%B5%D1%82%D0%B8%D0%BA%D0%BE%D0%B9-a2e2f86b2592
https://www.programiz.com/dsa/rabin-karp-algorithm

"""
alphabet = 256 
def search_with_Rabin_Karp(pattern, text):
    M = len(pattern)
    N = len(text)
    Q = 997
    hash_pattern = 0 
    hash_text = 0 
    hash = 1
    checking_5 = False
    
    for i in range(M-1):
        hash = (hash * alphabet) % Q 
    
    for i in range(M):
        hash_pattern = (hash_pattern * alphabet + ord(pattern[i]))% Q
        hash_text = (hash_text * alphabet + ord(text[i]))% Q
    
    for i in range(N-M + 1):
        if hash_pattern == hash_text: 
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == M:
                print(f"Совпадение! Начальный индекс подстроки: {i}")
                checking_5 = True
        if i < N-M:
            hash_text = (alphabet*(hash_text-ord(text[i])*hash) + ord(text[i + M]))% Q
            if hash_text < 0:
                hash_text = hash_text + Q 
    return checking_5
