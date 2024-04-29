from tabulate import tabulate
m = ["", 'н', 'о', 'п', 'р', 'с', 'т', 'ф', 'х']
n = ['00000', '01001','10001','01100','10010','10100','00110','00011']
table = [m]
for i in range(0, len(n)):
    line = [m[i + 1]]
    for l in range(0, i):
        line.append(" ")
    line.append("-")
    for j in range(i + 1, len(n)):
        num = 0
        for k in range(0, len(n[i])):
            if n[i][k] != n[j][k]:
                num += 1
        line.append(str(num))
    table.append(line)
print("Таблица попарных расстояний")
print(tabulate(table, m, tablefmt="psql",numalign='center'))
