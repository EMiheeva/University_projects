from itertools import groupby
from collections import Counter
import re
string = "aaaaadggggggggggggggghtyiklooooop"
print(string)
amount = 1
final_string = ""
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        amount += 1
    else:
        a = string[i]
        final_string = final_string +str(amount)+string[i]+" "
        amount  = 1
if string[len(string)-1]!= string[len(string)-2]:
    final_string = final_string + str(amount) + string[len(string)-1]+" "
    print(final_string)
    final_string = final_string.split(" ")
    final_string.pop(len(final_string)-1)
    final_string1 = final_string[:]
    for i  in range(0,len(final_string)):
        final_string[i]=re.sub("[^0-9]","",final_string[i])
        final_string1[i]=re.sub("[^A-Za-z]","",final_string1[i])
    for i in range(0,len(final_string)-1):
        j = i+1
        c = 0
        while(final_string[i]==final_string[j]):
            a = final_string1[i]
            b = final_string1[j]
            final_string1[i]=a+b
            j += 1
            c += 1
        for p in range(1,c+1):
            final_string[i+p]=" "
            final_string1[i+p]=" "
    for i in range(0,len(final_string)-1):
        if(final_string1[i].find(" ")!= -1):
            final_string1[i]=" "
    final_string1 = [element for element, _ in groupby(final_string1)]
    c= Counter(final_string1)
    for _ in range(0, c[' ']):
        final_string1.remove(" ")
    final_string = [element for element, _ in groupby(final_string)]
    c= Counter(final_string)
    for _ in range(0, c[' ']):
        final_string.remove(" ")
    mas=[""]*len(final_string)
    for i in range(0, len(final_string)):
        mas[i]=final_string[i]+final_string1[i]
    print(*mas)
