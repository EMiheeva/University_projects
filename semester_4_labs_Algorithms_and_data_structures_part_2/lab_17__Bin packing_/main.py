''' Для данной задачи существует множество эвристических алгоритмов.
    Например, «в первый подходящий» (First Fit - FF), «в наилучший из подходящих» (Best Fit - BF), 
    «в первый подходящий с убыванием» (First Fit Decreasing - FFD) 
    и «в наилучший из подходящих с убыванием» (Best FitDecreasing - BFD).
    Рассмотрим BF (Best Fit - наилучший остаток) алгоритм
    Данный алгоритм помещает всякий предмет таким образом, чтобы после его укладки в ящике оставалось как можно меньше места. 
    Укладка в новый ящик происходит только в том случае, если очередной объект не помещается ни в какой из имеющихся ящиков.
    Источник теории: https://studfile.net/preview/10028589/page:28/
'''


def Best_Fit(elem, volume):
    
    bucket = {i:elem[i] for i in range(0, len(elem))} #создание словаря
    
    box = {0:[bucket[0]]} #присвоить ключу 0 значение 0
    
    for i in range(1, len(elem)): #ключ 0 занят, значит начинаем с 1
       
        minimum = float('inf')
        subject = i
        new_subject = -1

        if ( bucket[subject] > volume):
            print(f"Предмет под номером {i} [{bucket[i]}] > {const_V} - не помещается")
        
        else:
            for j in range(0, len(box)):
                if (round(volume - sum(box[j]), 1)) < minimum and (round(volume - sum(box[j]), 1)) >= bucket[subject]:
                    minimum = round(volume - sum(box[j]), 1) #формула с сайта! целая(round)часть суммы sum(box[j]) объемов предметов,
                                                             #это главная идея алгоритма!
                    new_subject = j
            
            if new_subject == -1:
                box[j+1] = [bucket[subject]] #+1 означает создание нового ящика
                #print(f"{box[j+1]} не помещается в ящик с эл-том {box[j]}")
            else: 
                #print(f"[{bucket[subject]}] помещается в ящик с эл-том {box[new_subject]}")
                box[new_subject].append(bucket[subject])

    print()
    print(f"Понадобится ящиков: {len(box)}")
    print(f"Содержимое ящиков, объем равен {const_V}:")
    for i in range(0, len(box)):
        print(f"ящик {i+1}: {box[i]}")
    print()

inp = open('input.txt', 'r')
line = inp.readline()
elements = line.split()
elements = list(map(lambda x : float(x), elements))

const_V = 10
Best_Fit(elements, const_V)
