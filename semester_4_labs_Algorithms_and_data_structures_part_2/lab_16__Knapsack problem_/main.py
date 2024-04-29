"""
Источник вдохновения (кода): https://towardsdatascience.com/choosing-fast-with-dynamic-programming-b6916da543f4

stuffdict = {'couch_s':(300,75), 
             'couch_b':(500,80), 
             'bed':(400,100), 
             'closet':(200,50), 
             'bed_s':(200,40), 
             'desk':(200,70), 
             'table':(300,80),
             'tv_table':(200,30),
             'armchair':(100,30),
             'bookshelf':(200,60), 
             'cabinet':(150,20),
             'game_table':(150,30),
             'hammock':(250,45),
             'diner_table_with_chairs':(250,70),
             'stools':(150,30),
             'mirror':(100,20),
             'instrument':(300,70),
             'plant_1':(25,10),
             'plant_2':(30,20),
             'plant_3':(45,25),
             'sideboard':(175,30),
             'chest_of_drawers':(25,40),
             'guest_bed':(250,40),
             'standing_lamp':(20,30), 
             'garbage_can':(30,35), 
             'bar_with_stools':(200,40), 
             'bike_stand':(100,80),
             'chest':(150,25),
             'heater':(100,25)
            }
"""

bag_from_file = {}
with open("stuff_and_things.txt") as input:
    for line in input:
        (key, value_1, value_2) = line.split()
        bag_from_file[key] = int(value_1), int(value_2) #потому что одному ключу надо присвоить два значения
                                     #couch_s <- ключ 300 75 <- его два значения одновременно
#самопроверка. как обратиться к элементам словаря
#print(bag_from_file['couch_s'][0])
#print(bag_from_file['couch_s'][1])
#for key, value1 in bag_from_file.items(): 
    #print(key, ':', value1)

def get_weight_and_cost(bag):
    weight_from_file = [bag[element][0] for element in bag]
    cost_from_file = [bag[element][1] for element in bag]        
    return weight_from_file, cost_from_file

#Идея псевдокода взята отсюда: https://neerc.ifmo.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BE_%D1%80%D1%8E%D0%BA%D0%B7%D0%B0%D0%BA%D0%B5#.D0.9C.D0.B5.D1.82.D0.BE.D0.B4_.D0.B4.D0.B8.D0.BD.D0.B0.D0.BC.D0.B8.D1.87.D0.B5.D1.81.D0.BA.D0.BE.D0.B3.D0.BE_.D0.BF.D1.80.D0.BE.D0.B3.D1.80.D0.B0.D0.BC.D0.BC.D0.B8.D1.80.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D1.8F
def create_table(bag, const_weight):
    weight, cost = get_weight_and_cost(bag)
    size_of_table = len(bag) 
      
    # создаём таблицу из нулевых значений
    TABLE = [[0 for a in range(const_weight+1)] for i in range(size_of_table+1)]

    for i in range(size_of_table+1):
        for j in range(const_weight+1):
            # базовый случай
            if i == 0 or j == 0:
                TABLE[i][j] = 0
            
            # если вес предмета меньше веса столбца,
            # максимизируем значение суммарной ценности
            elif j >= weight[i-1]: #это условие, что предмет попал!
                TABLE[i][j] = max(cost[i-1] + TABLE[i-1][j-weight[i-1]], TABLE[i-1][j])
                  
            # если вес предмета больше веса столбца,
            # забираем значение ячейки из предыдущей строки
            else: #это условие, что предмет не попал!
                TABLE[i][j] = TABLE[i-1][j]       
    return TABLE, weight, cost

def find_stuff_and_things(bag, const_weight):
    TABLE, weight, cost = create_table(bag, const_weight)
    size_tablet = len(bag)
    check_point = TABLE[size_tablet][const_weight]# условие, проверяющее, когда рюкзак собран или в него
                                                # можно доложить предмет
    new_weight = const_weight
    result_weigth_and_cost = []
    index_stuff = []
    
    for i in range(size_tablet, 0, -1):  
    #собираем предметы с правого нижнего конца, чтобы понять, из каких именно предметов выходит такая максимальная стоимость рюкзака!
        if check_point <= 0:  
            break
        if check_point == TABLE[i-1][new_weight]:  
            continue
        else: 
            result_weigth_and_cost.append((weight[i-1], cost[i-1]))
            index_stuff.append(i-1)
            check_point -= cost[i-1]   
            new_weight -= weight[i-1]  
    
    #print(f"Индексы предметов в рюкзаке: {index_stuff}")        
    result_stuff = []
    for i in range (len(index_stuff)):
        result_stuff.append(list(bag_from_file.keys())[index_stuff[i]]) 
    #print(f"Сами предметы: {result_stuff}")
    
    return result_stuff, result_weigth_and_cost
        
#выдумали обходной путь, как получить конкретные предметы
#зная, что словарь не упорядочен и не индексируется: https://qna.habr.com/q/793941
#                                                    https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
#my_dict = [list(bag_from_file.keys())[4]]
#print(my_dict, type(my_dict))

const_weight = 1750
STUFF, WEIGHT_and_COST = find_stuff_and_things(bag_from_file, const_weight)
result_weight = sum(WEIGHT_and_COST[element][0] for element in range (len(WEIGHT_and_COST)))
result_cost = sum(WEIGHT_and_COST[element][1] for element in range (len(WEIGHT_and_COST)))

print(f"Что кладем в рюкзак: \n{STUFF} \nИх вес и цена соответвенно: \n{WEIGHT_and_COST}")
print(f"Объем рюкзака: {const_weight} \nВес предметов: {result_weight} \nЦена предметов(макс.стоимость рюкзака): {result_cost}")
