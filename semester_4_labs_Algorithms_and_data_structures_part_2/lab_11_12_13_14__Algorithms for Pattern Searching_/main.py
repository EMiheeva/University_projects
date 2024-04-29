import AVTO
import KMP
import BAD
import GOOD
import RK
file_inp = open('input.txt', 'r')
text = file_inp.read()
print(f"Строка из файла: {text}")
pattern = input("Введите образец: ")
print()
print("Конечный автомат")
check_1 = AVTO.search_with_FA(pattern, text)
if check_1 == False:
    print("Образец не найден")
print()
print("Кнут Морис Пратт")
check_2 = KMP.search_with_Knuth_Morris_Pratt(pattern, text)
if check_2 == False:
    print("Образец не найден")
print()
print("Бойер-Мур. Плохая евристика")
check_3 = BAD.search_with_bad(pattern, text)
if check_3 == False:
    print("Образец не найден")
print()
print("Бойер-Мур. Хорошая евристика")
check_4 = GOOD.search_with_good(pattern,text)
if check_4 == False:
    print("Образец не найден")
print()
print("Рабин-Карп")
check_5 = RK.search_with_Rabin_Karp(pattern, text)
if check_5 == False:
    print("Образец не найден")
print()



