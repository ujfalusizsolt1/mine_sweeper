gameover = False

import random

table_list= []

for i in range(0,9):
    table_list.append([])
    for j in range(0,9):
        table_list[i].append(0)

for i in range(0,15):
    table_list[random.randint(0, 8)][random.randint(0, 8)] = 1


for i in range(0, 9):
    for j in range(0, 9):
        print(table_list[i][j], end=' ')
    print("")


#while gameover = False:
    

